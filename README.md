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
# same for CentOS:CentOS-7
osc api -X PUT -T CentOS-7-project.xml '/source/CentOS:CentOS-7/_meta'
osc api -X PUT -T CentOS-7-project-config.spec '/source/CentOS:CentOS-7/_config'

# create list of distributions:
osc api -T distributions.xml /distributions
```

Example - verifying satus of Repositories:
```bash
osc api /build/CentOS\:CentOS-8/_result
```

# Resources

My configuration files are based on these exports from 

```bash
osc api /distributions > distributions.xml

osc api /source/CentOS:CentOS-7/_meta > CentOS-7-project.xml
osc api /source/CentOS:CentOS-7/_config > CentOS-7-project-config.spec

osc api /source/CentOS:CentOS-8/_meta > CentOS-8-project.xml
osc api /source/CentOS:CentOS-8/_config > CentOS-8-project-config.spec
```

# Bugs


Some repositories show error, for example:
```bash
osc api /build/CentOS\:CentOS-8/_result
```
Errors:
```xml
<resultlist state="5ae06af69b69b32e92dc2b20df58a3d7">
 <!-- ... -->
  <result project="CentOS:CentOS-8" repository="powertools" arch="x86_64" code="broken" state="broken" details="unresolvable preinstalls: nothing provides rpm" />
  <result project="CentOS:CentOS-8" repository="extras" arch="x86_64" code="broken" state="broken" details="unresolvable preinstalls: nothing provides rpm" />
  <result project="CentOS:CentOS-8" repository="devel" arch="x86_64" code="broken" state="broken" details="unresolvable preinstalls: nothing provides rpm" />
  <result project="CentOS:CentOS-8" repository="cloud" arch="x86_64" code="broken" state="broken" details="unresolvable preinstalls: nothing provides rpm" />
  <result project="CentOS:CentOS-8" repository="appstream" arch="x86_64" code="broken" state="broken" details="unresolvable preinstalls: nothing provides rpm" />
 <!-- ... -->
</resultlist>
```

I suspect that dependencies in CentOS-8-project.xml are simply bogus...



