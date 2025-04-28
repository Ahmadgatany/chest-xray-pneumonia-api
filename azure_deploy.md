# Deploy Chest X-Ray Pneumonia API to Azure

This document describes how to deploy the Chest X-Ray Pneumonia API using Docker and Azure App Service.

---

## Prerequisites

- Azure subscription
- Docker installed locally
- Azure CLI installed
- Azure Container Registry (ACR) created
- Azure App Service plan created

---

## 1. Build the Docker Image

From the project root directory, build the Docker image:

```bash
docker build -t chest-xray-pneumonia-api .
```

---

## 2. Tag the Docker Image

Tag the image for your Azure Container Registry:

```bash
docker tag chest-xray-pneumonia-api <your-registry-name>.azurecr.io/chest-xray-pneumonia-api:latest
```

Replace `<your-registry-name>` with your actual Azure Container Registry name.

---

## 3. Push the Image to Azure Container Registry

Login to your Azure Container Registry:

```bash
az acr login --name <your-registry-name>
```

Push the Docker image:

```bash
docker push <your-registry-name>.azurecr.io/chest-xray-pneumonia-api:latest
```

---

## 4. Deploy the Container on Azure App Service

1. Go to Azure Portal.
2. Create a **Web App for Containers**.
3. Configure the app to pull the container image from your Azure Container Registry.
4. Set the container port under Application Settings:
   - Add a new setting: `WEBSITES_PORT = 8000`
5. Save and restart the app.

---

## 5. Access the API

Once the deployment is complete, you can access your API:

```
https://<your-app-name>.azurewebsites.net/docs
```

The `/docs` endpoint provides an interactive Swagger UI to test your API.

---

## Project Structure Overview

```
chest-xray-pneumonia-api/
├── app/
│   ├── config.py
│   ├── main.py
│   ├── loaders/
│   ├── routes/
│   └── utils/
├── tests/
├── notebooks/
├── saved_models/
├── Dockerfile
├── README.md
├── azure_deploy.md
├── requirements.txt
```

---

## Common Issues

| Issue                         | Solution                                                              |
|--------------------------------|-----------------------------------------------------------------------|
| App not starting               | Ensure `WEBSITES_PORT` is set to `8000`                               |
| Image pull failure             | Confirm that the Azure App Service has access to the ACR              |
| CrashLoopBackOff errors        | Check application logs in Azure Portal                               |
| 502 Bad Gateway error          | Ensure the container is exposing and listening to the correct port   |

---

## Notes

- Every time you update the code, you must rebuild, retag, and push the Docker image.
- You can monitor container logs through Azure Portal or Azure CLI using:

```bash
az webapp log tail --name <your-app-name> --resource-group <your-resource-group>
```

---

## Contact

For any questions or support regarding the deployment, please refer to the GitHub Issues section.

---

