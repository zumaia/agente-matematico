#!/usr/bin/env python3
"""Arranca `app.py` y `green_app.py` en procesos separados y reenvía sus salidas.

Uso:
  python3 scripts/start_both.py

El script captura SIGINT/SIGTERM y termina ambos procesos ordenadamente.
"""
import subprocess
import signal
import sys
import threading
import os


PROCS = []


def _stream_output(prefix, stream):
    for line in iter(stream.readline, b""):
        try:
            sys.stdout.buffer.write(f"[{prefix}] ".encode('utf-8') + line)
            sys.stdout.flush()
        except Exception:
            # Fallback texto
            try:
                print(f"[{prefix}] " + line.decode('utf-8', errors='ignore'), end='')
            except Exception:
                pass


def start_process(cmd, name, env=None):
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=False,
        env=env,
    )

    t = threading.Thread(target=_stream_output, args=(name, p.stdout), daemon=True)
    t.start()

    PROCS.append((p, name))
    return p


def stop_all():
    print('\nDeteniendo procesos...')
    for p, name in PROCS:
        if p.poll() is None:
            try:
                print(f"Terminando {name} (pid={p.pid})")
                p.terminate()
            except Exception:
                pass

    # Esperar un poco y forzar kill si siguen vivos
    for p, name in PROCS:
        try:
            p.wait(timeout=5)
        except Exception:
            try:
                print(f"Forzando kill a {name} (pid={p.pid})")
                p.kill()
            except Exception:
                pass


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    python = sys.executable or 'python3'

    # Comandos: ejecutar los módulos por archivo para mantener comportamientos en __main__
    app_cmd = [python, os.path.join(root, 'app.py')]
    green_cmd = [python, os.path.join(root, 'green_app.py')]

    # Entorno heredado (permite usar variables existentes)
    env = os.environ.copy()

    print('Iniciando app.py ...')
    p1 = start_process(app_cmd, 'APP', env=env)

    print('Iniciando green_app.py ...')
    p2 = start_process(green_cmd, 'GREEN', env=env)

    def _handle_sig(signum, frame):
        stop_all()
        sys.exit(0)

    signal.signal(signal.SIGINT, _handle_sig)
    signal.signal(signal.SIGTERM, _handle_sig)

    # Esperar a que alguno de los procesos termine
    try:
        while True:
            alive = [p for p, _ in PROCS if p.poll() is None]
            if not alive:
                break
            for p, name in PROCS:
                if p.poll() is not None:
                    print(f"Proceso {name} finalizó con código {p.returncode}")
            # pequeño sleep
            signal.pause()
    except Exception:
        # signal.pause puede fallar en Windows; usar un simple bucle
        try:
            while any(p.poll() is None for p, _ in PROCS):
                for p, name in PROCS:
                    if p.poll() is not None:
                        print(f"Proceso {name} finalizó con código {p.returncode}")
                import time

                time.sleep(0.5)
        except KeyboardInterrupt:
            stop_all()

    stop_all()


if __name__ == '__main__':
    main()
