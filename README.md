<b>Automated CI/CD Pipeline for Web Applications Using Jenkins and GitHub</b>

This is my Portfolio Project for the Foundations Year at ALX Africa and Holberton School. It is an Automated CI/CD Pipeline for Web Applications, using technologies like Jenkins and GitHub, and also getting deployed in Docker.

* Jenkins Web Interface: <http://107.23.96.11:8080/job/Portfolio-Project>
* Blog Article: <https://www.dev.to/>
* Author's LinkedIn: <https://www.linkedin.com/in/madubuike-emmanuel>
* Author's Twitter: <https://www.twitter.com/0xNuel>

![Screenshot from 2023-06-07 15-24-26](https://github.com/NuelUzoma/Portfolio-Project/assets/107211055/523f029e-b113-4e5e-9597-51c930e2b00f)


![Screenshot from 2023-06-15 03-52-47](https://github.com/NuelUzoma/Portfolio-Project/assets/107211055/6a38f0f2-7577-433a-8855-c01228e58a97)

**Method of Installation**

This is a CI/CD Pipeline for Web Application Using Jenkins, GitHub and Docker.
* Install Jenkins: Jenkins must be installed with a Java Development Kit (JDK) for proper functionality. Steps for successful installation of both can be found at <https://www.jenkins.io/doc/book/installing/linux/>, for Linux environments. The port 8080 must be allowed if a firewall is set up on your server.
* Install Docker: Docker can also be installed by visiting <https://docs.docker.com/engine/install/ubuntu/> for an Ubuntu environment and following all the steps given.
* GitHub: No prior installation is needed for GitHub. Login into your GitHub and create a new repository needed for the project.

**Usage**

This project defines with three main technologies namely Jenkins, GitHub and Docker. Jenkins makes use of Webhooks provided by GitHub to integrate with it. Webhooks serves as a trigger between Jenkins and GitHub. Once code changes as been pushed to GitHub, it triggeers Jenkins automatically through Webhooks. It serves as a pipeline, automated for Build, Test and Deploy purposes with Docker. Jenkins server was installed on my web-01 server for public internet for usage for webhooks and Docker server was installed on my web-02 server for easier integration with Jenkins for Test and Deploy purposes with containers. To deploy with Docker, certain build steps and configurations as to be met with Jenkins.

**Contribution**

For contributions, send a mail to <emmanuelmadubuike.dev@gmail.com> to obtain the credentials for Jenkins before opening a pull request in order to access the Jenkins server for the project.

**Related Projects**

This is the first project I have worked on concerning this field. There are currently no related projects to this project. I look forward to the future if related projects are going to come out on this.

**Licensing**

There is no certain license currently obtained for this project. Currently working on getting an MIT License.
