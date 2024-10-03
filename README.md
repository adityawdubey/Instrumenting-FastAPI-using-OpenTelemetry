# Instrumenting-FastAPI-using-OpenTelemetry

This project demonstrates how to instrument FastAPI applications using OpenTelemetry and visualize the traces using **Grafana** and **Tempo**. This setup helps you monitor, trace, and analyze the performance of FastAPI-based microservices and pinpoint bottlenecks or issues across distributed systems.

For a detailed walkthrough and additional insights, check out my blog post: [Instrumenting FastAPI Services with OpenTelemetry, Grafana, and Tempo.](https://adityadubey.cloud/instrumenting-fastapi-services-with-opentelemetry-grafana-and-tempo)

![Blank diagram (7) copy](https://github.com/user-attachments/assets/3edd12cb-c763-4d98-ba3a-f3e53d22a569)

# Table of Contents

1. [Overview](#overview)
2. [Technologies Used](#️technologies-used)
3. [Getting Started](#getting-started)
   - [Clone the repository](#1-clone-the-repository)
   - [Deploy Services](#2-deploy-services)
     - [Build Docker Images for Your FastAPI Services](#-build-docker-images-for-your-fastapi-services)
     - [Deploy FastAPI Services on k8s](#-deploy-fastapi-services-on-k8s)
     - [Install Grafana and Tempo](#-install-grafana-and-tempo)
     - [Port forward to access services](#-port-forward-to-access-services)
     - [Add Tempo data source](#-add-tempo-data-source)
4. [Usage](#usage)
   - [Open `service_a` docs and send req to `service b`](#⁠⁠open-service_a-docs-and-send-req-to-service-b)
   - [Check Tempo explore](#check-tempo-explore)
5. [Contributing](#contributing) 

# Overview

This repository contains a sample FastAPI project instrumented with OpenTelemetry. It showcases how you can trace API requests, monitor service performance, and use Grafana and Tempo for visualizing these traces.

This project is ideal if you want to:

- Gain insights into your FastAPI application’s performance.
- Set up distributed tracing for better observability in a microservices architecture.
- Use open-source observability tools like Grafana, Tempo, and Prometheus.

# ️Technologies Used

- **FastAPI**: A high-performance, Python web framework for building APIs.
- **OpenTelemetry**: An open-source framework for collecting telemetry data (traces, metrics, logs) across various programming languages and systems.
- **Docker**: For containerizing applications.
- **Kubernetes**: For deploying applications in a containerized environment.
- **Grafana**: For visualizing traces.
- **Tempo**: For storing and querying traces.


# Getting Started


## 1. Clone the repository:

```
git clone https://github.com/your-username fastapi-opentelemetry-demo.git
```

## 2. Deploy Services


If you plan to deploy using Docker or Kubernetes, follow the specific instructions within the codebase for building Docker images and deploying services.


### ❏ Build Docker Images for Your FastAPI Services

Containerize your FastAPI applications so that they can be deployed in a consistent and reproducible environment, whether locally or in Kubernetes. To do this, navigate to each service’s directory and run the following Docker build commands:

```
docker build -t service_a -f service_a/Dockerfile   
docker tag service_a aniketdubey/service_a:latest   
docker push adityadubey/service_a:latest
```

```
docker build -t service_b -f service_b/Dockerfile
docker tag service_b adityadubey/service_b:latest
docker push aniketdubey/service_b:latest
```

These commands create Docker images for both `service_a` and `service_b`. The `-t` flag assigns a tag (name) to each image, which is essential for identifying and deploying the containers later on.

### ❏ Deploy FastAPI Services on k8s

Create a dedicated namespace for the FastAPI microservices to organize resources more effectively:

```
kubectl create namespace fastapi
```

Once the namespace is created, you can deploy `service_a` and `service_b` by applying their respective YAML files (which should define the necessary Kubernetes configurations like deployments, services, etc.)

```
kubectl apply -f service_a.yaml  
kubectl apply -f service_b.yaml
```

### ❏ Install Grafana and Tempo

To monitor and trace the behavior of your microservices, Install Grafana (for visualization) and Tempo (for storing and querying traces).

```
helm repo add grafana https://grafana.github.io/helm-charts
helm install grafana grafana/grafana -n fastapi   
helm install tempo grafana/tempo -n fastapi
```

These commands will set up Grafana and Tempo in your Kubernetes environment, preparing them to receive and visualize traces from your FastAPI services.

### ❏ Port forward to access services

Once your services and observability stack are deployed, you'll need to access them. In a typical Kubernetes setup, you can use port forwarding to expose your services locally.

``` 
kubectl port-forward svc/grafana 3000:80
```

You can now access Grafana by opening your browser and navigating to [http://localhost:3000](http://localhost:3000/)

Similarly,

```
kubectl port-forward svc/service-a-service 8000:8000
kubectl port-forward svc/service-b-service 8001:8001
```

### ❏ Add temp data source

With Grafana running, it’s time to integrate Tempo to visualize the traces collected from your FastAPI services. To do this:

1. Get grafana password  
    `kubectl get secret --namespace fastapi grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo`

2. Open Grafana in your browser ([`http://localhost:3000`](http://localhost:3000)) and log in (default credentials are usually `admin`/`admin`).
    
3. Navigate to **Configuration &gt; Data Sources**.
    
4. Click on **Add Data Source** and select **Tempo** from the list.
    
5. Enter the necessary details for Tempo (usually the default settings should work if Tempo is installed correctly).
    
6. Save the configuration.

    <img width="1439" alt="Screenshot 2024-10-02 at 12 24 42 AM (1)" src="https://github.com/user-attachments/assets/8528f9e1-727b-406c-a2b8-cef6fbb79ea9">

## Usage

### ⁠⁠Open `service_a` docs and send req to `service b`

![Screenshot 2024-10-02 at 12 56 47 PM](https://github.com/user-attachments/assets/7139b5d7-444d-486a-a670-2f6df4c3925f)

### Check tempo explore

Once Tempo is integrated, you can explore your trace data in Grafana using the **Explore** tab. Traces from **Service A** to **Service B** will be displayed.

<img width="1440" alt="Screenshot 2024-10-02 at 12 24 22 AM" src="https://github.com/user-attachments/assets/cd385394-2368-4eab-a304-4860e4305ffe">

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to improve the project.


