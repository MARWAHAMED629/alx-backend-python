# Jenkins Setup Guide

This guide will help you set up Jenkins for the Django Messaging App CI/CD pipeline.

## Prerequisites

- Docker installed on your system
- GitHub repository with the messaging app code
- Docker Hub account (for pushing images)

## Step 1: Install Jenkins

Run the following command to start Jenkins in a Docker container:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

This command:
- Pulls the latest LTS Jenkins image
- Exposes Jenkins on port 8080
- Maps the Jenkins home directory to persist data
- Runs Jenkins in detached mode

## Step 2: Access Jenkins

1. Open your browser and go to `http://localhost:8080`
2. Wait for Jenkins to start up (this may take a few minutes)
3. Get the initial admin password by running:
   ```bash
   docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
   ```

## Step 3: Install Required Plugins

1. Click "Install suggested plugins" or "Select plugins to install"
2. Make sure the following plugins are installed:
   - **Git plugin** - For pulling code from GitHub
   - **Pipeline plugin** - For creating Jenkins pipelines
   - **ShiningPanda plugin** - For Python support
   - **Cobertura plugin** - For code coverage reports
   - **JUnit plugin** - For test results
   - **Docker plugin** - For Docker operations
   - **Credentials Binding plugin** - For managing secrets

## Step 4: Configure Credentials

### GitHub Credentials

1. Go to **Manage Jenkins** > **Manage Credentials**
2. Click **System** > **Global credentials** > **Add Credentials**
3. Choose **Username with password**
4. Set the following:
   - **Kind**: Username with password
   - **Scope**: Global
   - **Username**: Your GitHub username
   - **Password**: Your GitHub personal access token
   - **ID**: `github-credentials`
   - **Description**: GitHub credentials

### Docker Hub Credentials

1. Go to **Manage Jenkins** > **Manage Credentials**
2. Click **System** > **Global credentials** > **Add Credentials**
3. Choose **Username with password**
4. Set the following:
   - **Kind**: Username with password
   - **Scope**: Global
   - **Username**: Your Docker Hub username
   - **Password**: Your Docker Hub password/token
   - **ID**: `docker-hub-credentials`
   - **Description**: Docker Hub credentials

## Step 5: Create Pipeline Job

1. Click **New Item** on the Jenkins dashboard
2. Enter a name for your job (e.g., "messaging-app-pipeline")
3. Select **Pipeline** and click **OK**
4. Configure the pipeline:

### General Configuration
- **Description**: "Django Messaging App CI/CD Pipeline"
- Check **GitHub project** and enter your repository URL

### Pipeline Configuration
- **Definition**: Pipeline script from SCM
- **SCM**: Git
- **Repository URL**: Your GitHub repository URL
- **Credentials**: Select your GitHub credentials
- **Branch Specifier**: `*/main` (or your default branch)
- **Script Path**: `messaging_app/Jenkinsfile`

### Build Triggers
- Check **Poll SCM** and set schedule to `H/5 * * * *` (every 5 minutes)
- Or check **GitHub hook trigger for GITScm polling** for webhook-based triggers

## Step 6: Configure Webhooks (Optional)

To trigger builds automatically on GitHub pushes:

1. Go to your GitHub repository
2. Go to **Settings** > **Webhooks**
3. Click **Add webhook**
4. Set **Payload URL** to: `http://your-jenkins-url/github-webhook/`
5. Set **Content type** to: `application/json`
6. Select **Just the push event**
7. Click **Add webhook**

## Step 7: Update Jenkinsfile

Make sure your `Jenkinsfile` has the correct Docker Hub username:

```groovy
environment {
    DOCKER_IMAGE = 'your-dockerhub-username/messaging-app'
    DOCKER_TAG = "${env.BUILD_NUMBER}"
}
```

Replace `your-dockerhub-username` with your actual Docker Hub username.

## Step 8: Test the Pipeline

1. Go to your pipeline job
2. Click **Build Now**
3. Monitor the build logs to ensure everything works correctly

## Troubleshooting

### Common Issues

1. **Permission Denied**: Make sure Jenkins has the necessary permissions to access your repository
2. **Docker Permission Issues**: Add Jenkins user to the docker group or run Jenkins with Docker privileges
3. **Plugin Installation Failures**: Restart Jenkins and try installing plugins again
4. **Credential Issues**: Double-check your GitHub and Docker Hub credentials

### Useful Commands

```bash
# View Jenkins logs
docker logs jenkins

# Restart Jenkins
docker restart jenkins

# Access Jenkins shell
docker exec -it jenkins bash

# Stop Jenkins
docker stop jenkins

# Remove Jenkins container
docker rm jenkins
```

## Next Steps

After setting up Jenkins:

1. Push your code to GitHub
2. Trigger a manual build in Jenkins
3. Monitor the build logs
4. Check the generated reports (test results, coverage)
5. Verify that Docker images are pushed to Docker Hub

## Security Considerations

- Use strong passwords and tokens
- Regularly update Jenkins and plugins
- Limit access to Jenkins to authorized users only
- Use HTTPS for Jenkins if exposed to the internet
- Regularly backup Jenkins data 