import subprocess

def create_kubernetes_cluster():
    try:
        
        command = "minikube start --vm-driver=docker"
        subprocess.run(command, shell=True, check=True)
        print("Clúster de Kubernetes creado con éxito con Minikube utilizando Docker")
    except subprocess.CalledProcessError as e:
        print("Error al crear el clúster de Kubernetes:", e)

if __name__ == "__main__":
    create_kubernetes_cluster()
