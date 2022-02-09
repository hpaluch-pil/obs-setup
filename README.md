# obs-setup

Files used to setup my on-premise openSUSE Build Service - https://build.opensuse.org/

# Requirements

You need to have running on-premise (also called "private installation") OBS.

Then you have call API in this order:

```bash
# creates Project: CentOS:CentOS-8
osc api -X PUT -T CentOS-8-project.xml '/source/CentOS:CentOS-8/_meta'
# adds Project Config to  project CentOS:CentOS-8
osc api -X PUT -T CentOS-8-project-config.spec '/source/CentOS:CentOS-8/_config'
# TODO: setup also CentOS-7
# ..

# create list of distributions:
osc api -T distributions.xml /distributions
```

# Resources

My configuration files are based on these exports from 

```bash
osc api /distributions > distributions.xml
osc api /source/CentOS:CentOS-8/_meta > CentOS-8-project.xml
osc api /source/CentOS:CentOS-8/_config > CentOS-8-project-config.spec
```

