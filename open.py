import subprocess

def open_terminal(comando):
    subprocess.run(["gnome-terminal -e " + comando], shell=True, check=True)

def run_command(comando):
    subprocess.call([comando], shell=True)

if __name__ == "__main__":
    # Abre una terminal y ejecuta el comando ls
    open_terminal("sh run-app.sh")

    # Abre otra terminal y ejecuta el comando ps
    open_terminal("ls")

    # Ejecuta el comando date en la terminal actual
    run_command("date")