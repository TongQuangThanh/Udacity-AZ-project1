# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

# Analysis

**Costs**: App service would be more flexible since more than one app can be made to share the App Service plan. VM has the advantage of being able to be de-allocated when not in use. Beside of it, if VM is install Licensed operating system, so our cost is include OS license and so in general, App service is cheaper than VM in same hardware configuration.
Example:
730h * 1 **VM** on West US with Standard Window OS with instance A1 hardware 1Cores, 1.75GB RAM + 70GB temp storage cost **$65.70**
730h * 1 **App Service** on West US with Window OS with instance B1 hardware 1Cores, 1.75GB RAM + 70GB temp storage cost **$54.75**

**Scalability**: Both the VM and the App Service can be scaled. But App service is has built-in service and integrated. So no need to config any more scalability to work on App service.

**Availability**: Both VM and App Service have Multi region failover for availability but VM generally have more availability with more complicated thing compare to App Service, so it may require some or many setup and configuration to be fault tolerant and avoid downtimes during maintenance and upgrades depend on set of VMs.

**Workflow**: App Service has easier to deploy applications than to Virtual Machines. And a VM is IaaS so we need config/prepare environment to run our project and then deploy our project while just need to deploy our project when App Service may provide suitable environment for our project

# Choose solution
                        | We are deploying a light-weight and small web app                                             |
Our project description | Initial size, network traffic, resource work load are small fit for App Service               | => App Service is the good choice for us
                        | Also require environment is not complicated                                                   |
                        | And **App Services** cost less than **VMs**                                                   |

# Justification
An App Service is a PaaS so we just need to deploy code and not worry about the requirement environment. It also has good pricing tiers and enough for scalability. Beside of it, App Service provide many options that help us to integrate source code and deploy application to production workflow

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

If our app increase size and traffic, also more role to be evoke, more manage should be consider
so we can migrate to VMs for better performance of growing project

Because of App Service limit to 4 cores of CPU and 7GB RAM and 10GB of storage so if application need higher compute performance and need more hardware configuration than App Service maximum quota. Now time to choose a VM for better performance. Beside of it, when our application is bigger, maybe our system has extend with more complicated tools/configuration/require other software/service from any other resource/source. So VM is the best fit for this situation because it give us more control and full manage of system