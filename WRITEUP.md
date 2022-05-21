# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

We are deploying a light-weight and small web app
Initial size, network traffic, resource work load are small fit for App Service
Also require environment is not complicated
And **App Services** cost less than **VMs** on this situation so it is a good choice for us

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

If our app increase size and traffic, also more role to be evoke, more manage should be consider
so we can migrate to VMs for better performance of growing project