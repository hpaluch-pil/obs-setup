# from: osc api /source/CentOS:CentOS-8/_config
Repotype: rpm-md

# Modules enabled by default
ExpandFlags: module:common preinstallexpand
Preinstall: rpm
Preinstall: perl-interpreter perl-Digest-MD5

VMinstall: device-mapper iptables-libs

# From Fedora 31 and later
FileProvides: /usr/bin/fipscheck  fipscheck
FileProvides: /usr/bin/db_stat    libdb-utils
FileProvides: /usr/bin/gpg2 gnupg2
FileProvides: /usr/bin/python python-unversioned-command
FileProvides: /usr/bin/python2 python2
FileProvides: /usr/bin/python3 python3

# CentOS 8 special:
FileProvides: /usr/bin/ruby       ruby
FileProvides: /usr/libexec/platform-python platform-python
FileProvides: /usr/bin/gdb-add-index gdb-headless

Required: autoconf automake binutils bzip2 gcc gdbm gettext glibc perl-Digest-MD5
Required: perl perl-constant perl-Carp perl-Data-Dumper perl-Exporter perl-Getopt-Long
Required: libtool ncurses zlib rpm-build centos-release redhat-rpm-config gcc-c++
Keep: autoconf automake binutils bzip2 gcc gdbm gettext glibc perl-Digest-MD5
Keep: perl perl-constant perl-Carp perl-Data-Dumper perl-Exporter perl-Getopt-Long
Keep: libtool ncurses zlib rpm-build centos-release redhat-rpm-config gcc-c++
Keep: rpm-build-libs

# break dependency cycles at defined states
Order: filesystem:vim-filesystem
Order: filesystem:acl
Order: filesystem:attr
Order: filesystem:libgcc
Order: filesystem:setup
Order: filesystem:bash
Order: filesystem:glibc

Support: bind-libs bind-utils bison cpio cpp cracklib
Support: e2fsprogs file findutils flex gawk gettext-devel
Support: glibc-devel gpm gzip info less
Support: make man mktemp module-init-tools
Support: ncurses-devel net-tools openssl
Support: patch procps psmisc strace
Support: unzip util-linux zlib-devel vim-enhanced
Support: shadow-utils initscripts bzip2-devel

# copied from mock config
Support: tar gcc-c++ redhat-rpm-config redhat-release which xz sed make bzip2 gzip gcc coreutils unzip shadow-utils diffutils cpio bash gawk rpm-build info patch util-linux findutils grep

Prefer: centos-repos(8):centos-linux-repos
Prefer: centos-linux-release:centos-linux-repos

Prefer: xorg-x11-libs libpng fam mozilla mozilla-nss xorg-x11-Mesa
Prefer: unixODBC libsoup glitz java-1_4_2-sun gnome-panel
Prefer: desktop-data-SuSE gnome2-SuSE mono-nunit gecko-sharp2
Prefer: apache2-prefork openmotif-libs ghostscript-mini gtk-sharp
Prefer: glib-sharp libzypp-zmd-backend mDNSResponder

Prefer: gnome-sharp2:art-sharp2 gnome-sharp:art-sharp
Prefer: ifolder3:gnome-sharp2 ifolder3:gconf-sharp2
Prefer: nautilus-ifolder3:gnome-sharp2
Prefer: gconf-sharp2:glade-sharp2 gconf-sharp:glade-sharp
Prefer: tomboy:gconf-sharp tomboy:gnome-sharp
Prefer: zmd:libzypp-zmd-backend
Prefer: yast2-packagemanager-devel:yast2-packagemanager
Prefer: docbook-utils:lynx
Prefer: xmlto:lynx

Prefer: syslogd sysklogd

Prefer: coreutils curl libcurl

Prefer: -libgcc-mainline -libstdc++-mainline -gcc-mainline-c++
Prefer: -libgcj-mainline -viewperf -compat -compat-openssl097g
Prefer: -zmd -OpenOffice_org -pam-laus -libgcc-tree-ssa -busybox-links
Prefer: -crossover-office -kernel-debug -qt3-devel

# since CentOS 7.4
Prefer: font(:lang=en)
Prefer: dejavu-sans-fonts

Conflict: ghostscript-library:ghostscript-mini

Ignore: centos-release:centos-repos
Ignore: centos-release:centos-repos(8)
Ignore: initscripts:kernel,udev,ethtool,mingetty
Ignore: tetex:tetex-fonts,desktop-file-utils
Ignore: pam:glib2
Ignore: libraw1394:kernel

Ignore: gettext-devel:libgcj,libstdc++-devel
Ignore: pam-modules:resmgr
Ignore: rpm:suse-build-key,build-key
Ignore: bind-utils:bind-libs
Ignore: alsa:dialog,pciutils
Ignore: portmap:syslogd
Ignore: fontconfig:freetype2
Ignore: fontconfig-devel:freetype2-devel
Ignore: xorg-x11-libs:freetype2
Ignore: xorg-x11:x11-tools,resmgr,xkeyboard-config,xorg-x11-Mesa,libusb,freetype2,libjpeg,libpng
Ignore: apache2:logrotate
Ignore: arts:alsa,audiofile,resmgr,libogg,libvorbis
Ignore: kdelibs3:alsa,arts,pcre,OpenEXR,aspell,cups-libs,mDNSResponder,krb5,libjasper
Ignore: kdelibs3-devel:libvorbis-devel
Ignore: kdebase3:kdebase3-ksysguardd,OpenEXR,dbus-1,dbus-1-qt,hal,powersave,openslp,libusb
Ignore: kdebase3-SuSE:release-notes
Ignore: jack:alsa,libsndfile
Ignore: libxml2-devel:readline-devel
Ignore: gnome-vfs2:gnome-mime-data,desktop-file-utils,cdparanoia,dbus-1,dbus-1-glib,krb5,hal,libsmbclient,fam,file_alteration
Ignore: libgda:file_alteration
Ignore: gnutls:lzo,libopencdk
Ignore: gnutls-devel:lzo-devel,libopencdk-devel
Ignore: pango:cairo,glitz,libpixman,libpng
Ignore: pango-devel:cairo-devel
Ignore: cairo-devel:libpixman-devel
Ignore: libgnomeprint:libgnomecups
Ignore: libgnomeprintui:libgnomecups
Ignore: orbit2:libidl
Ignore: orbit2-devel:libidl,libidl-devel,indent
Ignore: qt3:libmng
Ignore: qt-sql:qt_database_plugin
Ignore: gtk2:libpng,libtiff
Ignore: libgnomecanvas-devel:glib-devel
Ignore: libgnomeui:gnome-icon-theme,shared-mime-info
Ignore: scrollkeeper:docbook_4,sgml-skel
Ignore: gnome-desktop:libgnomesu,startup-notification
Ignore: python-devel:python-tk
Ignore: gnome-pilot:gnome-panel
Ignore: gnome-panel:control-center2
Ignore: gnome-menus:kdebase3
Ignore: gnome-main-menu:rug
Ignore: libbonoboui:gnome-desktop
Ignore: postfix:pcre
Ignore: docbook_4:iso_ent,sgml-skel,xmlcharent
Ignore: control-center2:nautilus,evolution-data-server,gnome-menus,gstreamer-plugins,gstreamer,metacity,mozilla-nspr,mozilla,libxklavier,gnome-desktop,startup-notification
Ignore: docbook-xsl-stylesheets:xmlcharent
Ignore: liby2util-devel:libstdc++-devel,openssl-devel
Ignore: yast2:yast2-ncurses,yast2-theme-SuSELinux,perl-Config-Crontab,yast2-xml,SuSEfirewall2
Ignore: yast2-core:netcat,hwinfo,wireless-tools,sysfsutils
Ignore: yast2-core-devel:libxcrypt-devel,hwinfo-devel,blocxx-devel,sysfsutils,libstdc++-devel
Ignore: yast2-packagemanager-devel:rpm-devel,curl-devel,openssl-devel
Ignore: yast2-devtools:perl-XML-Writer,libxslt,pkgconfig
Ignore: yast2-installation:yast2-update,yast2-mouse,yast2-country,yast2-bootloader,yast2-packager,yast2-network,yast2-online-update,yast2-users,release-notes,autoyast2-installation
Ignore: yast2-bootloader:bootloader-theme
Ignore: yast2-packager:yast2-x11
Ignore: yast2-x11:sax2-libsax-perl
Ignore: openslp-devel:openssl-devel
Ignore: java-1_4_2-sun:xorg-x11-libs
Ignore: java-1_4_2-sun-devel:xorg-x11-libs
Ignore: kernel-um:xorg-x11-libs
Ignore: tetex:xorg-x11-libs,expat,fontconfig,freetype2,libjpeg,libpng,ghostscript-x11,xaw3d,gd,dialog,ed
Ignore: yast2-country:yast2-trans-stats
Ignore: libgcc:glibc-32bit
Ignore: libstdc++:glibc-32bit
Ignore: susehelp:susehelp_lang,suse_help_viewer
Ignore: mailx:smtp_daemon
Ignore: cron:smtp_daemon
Ignore: hotplug:syslog
Ignore: pcmcia:syslog
Ignore: avalon-logkit:servlet
Ignore: jython:servlet
Ignore: ispell:ispell_dictionary,ispell_english_dictionary
Ignore: aspell:aspel_dictionary,aspell_dictionary
Ignore: smartlink-softmodem:kernel,kernel-nongpl
Ignore: OpenOffice_org-de:myspell-german-dictionary
Ignore: mediawiki:php-session,php-gettext,php-zlib,php-mysql,mod_php_any
Ignore: squirrelmail:mod_php_any,php-session,php-gettext,php-iconv,php-mbstring,php-openssl

Ignore: simias:mono(log4net)
Ignore: zmd:mono(log4net)
Ignore: horde:mod_php_any,php-gettext,php-mcrypt,php-imap,php-pear-log,php-pear,php-session,php
Ignore: xerces-j2:xml-commons-apis,xml-commons-resolver
Ignore: xdg-menu:desktop-data
Ignore: nessus-libraries:nessus-core
Ignore: evolution:yelp
Ignore: mono-tools:mono(gconf-sharp),mono(glade-sharp),mono(gnome-sharp),mono(gtkhtml-sharp),mono(atk-sharp),mono(gdk-sharp),mono(glib-sharp),mono(gtk-sharp),mono(pango-sharp)
Ignore: gecko-sharp2:mono(glib-sharp),mono(gtk-sharp)
Ignore: vcdimager:libcdio.so.6,libcdio.so.6(CDIO_6),libiso9660.so.4,libiso9660.so.4(ISO9660_4)
Ignore: libcdio:libcddb.so.2
Ignore: gnome-libs:libgnomeui
Ignore: nautilus:gnome-themes
Ignore: gnome-panel:gnome-themes
Ignore: gnome-panel:tomboy
Ignore: glibc:glibc-langpack

%ifnarch s390 s390x ppc ia64
Substitute: java2-devel-packages java-1_4_2-sun-devel
%else
 %ifnarch s390x
Substitute: java2-devel-packages java-1_4_2-ibm-devel
 %else
Substitute: java2-devel-packages java-1_4_2-ibm-devel xorg-x11-libs-32bit
 %endif
%endif

#
# SUSE compatibilities
#
Substitute: alsa alsa-lib
Substitute: alsa-devel alsa-lib-devel
Substitute: docbook-toys docbook-utils
Substitute: expat expat expat-devel
Substitute: libexpat-devel expat-devel
Substitute: gtkdoc gtk-doc
Substitute: db db4
Substitute: db-devel db4-devel
Substitute: dbus-1 dbus
Substitute: dbus-1-devel dbus-devel
Substitute: dbus-1-glib dbus-glib
Substitute: dbus-1-python dbus-python
Substitute: dbus-1-mono dbus-sharp
Substitute: gcc-fortran gcc-gfortran
Substitute: te_latex tetex-latex
Substitute: xorg-x11-devel  xorg-x11-proto-devel xorg-x11-xtrans-devel
Substitute: krb5 krb5-libs
Substitute: libbz2-devel bzip2-devel
Substitute: gtk-devel gtk+-devel
#Substitute: qt3 qt
#Substitute: qt3-devel qt-devel gcc-c++ libstdc++-devel
#Substitute: kdelibs3 kdelibs
#Substitute: kdelibs3-devel kdelibs-devel qt3-devel qt-devel gcc-c++ libstdc++-devel
#Substitute: kdegames3 kdegames
Substitute: libxerces-c-devel xerces-c-devel
Substitute: libsigc++2-devel libsigc++20-devel
Substitute: libgphoto2-devel gphoto2-devel
Substitute: libredland-devel redland-devel
Substitute: libraptor-devel raptor-devel
Substitute: librasqal-devel rasqal-devel
Substitute: openldap2 openldap
Substitute: openldap2-devel openldap-devel
Substitute: xorg-x11-Mesa-devel mesa-libGL-devel
Substitute: ImageMagick-Magick++-devel ImageMagick-c++-devel
Substitute: ImageMagick-Magick++ ImageMagick-c++
Substitute: pyxml PyXML
Substitute: pkg-config pkgconfig
Substitute: Mesa mesa-libGL
Substitute: Mesa-devel mesa-libGL-devel
Substitute: freetype2 freetype
Substitute: freetype2-devel freetype-devel
Substitute: liblcms-devel lcms-devel
Substitute: libqt4-devel qt4-devel

Prefer: -Glide3-libGL

Substitute: yast2-devel-packages docbook-xsl-stylesheets doxygen libxslt perl-XML-Writer popt-devel sgml-skel update-desktop-files yast2 yast2-devtools yast2-packagemanager-devel yast2-perl-bindings yast2-testsuite

# %ifarch x86_64 ppc64 s390x sparc64
# Substitute: glibc-devel-32bit glibc-devel-32bit glibc-32bit
# %else
#  %ifarch ppc
# Substitute: glibc-devel-32bit glibc-devel-64bit
#  %else
# Substitute: glibc-devel-32bit
#  %endif
# %endif

%ifarch %ix86
Substitute: kernel-binary-packages kernel-default kernel-smp kernel-bigsmp kernel-debug kernel-um kernel-xen kernel-kdump
%endif
%ifarch ia64
Substitute: kernel-binary-packages kernel-default kernel-debug
%endif
%ifarch x86_64
Substitute: kernel-binary-packages kernel-default kernel-smp kernel-xen kernel-kdump
%endif
%ifarch ppc
Substitute: kernel-binary-packages kernel-default kernel-kdump kernel-ppc64 kernel-iseries64
%endif
%ifarch ppc64
Substitute: kernel-binary-packages kernel-ppc64 kernel-iseries64
%endif
%ifarch s390
Substitute: kernel-binary-packages kernel-s390
%endif
%ifarch s390x
Substitute: kernel-binary-packages kernel-default
%endif

#
# experimentel, testing for mc
#
Substitute: sgml-skel sgml-common
Substitute: docbook-xsl-stylesheets docbook-style-xsl

Substitute: libelf elfutils-libelf

%define centos_version 800
%define centos 8
%define rhel 8

Macros:
%centos_version 800
%_vendor redhat

%centos 8
%centos_ver 8
%define rhel 8

#From RedHat buildsys-macros package
%rhel 8
%dist .el8
%el8 8

%kernel_module_package_buildreqs kernel-devel redhat-rpm-config

%ext_info .gz
%ext_man .gz

%info_add(:-:) test -x /sbin/install-info -a -f %{?2}%{?!2:%{_infodir}}/%{1}%ext_info && /sbin/install-info --info-dir=%{?2}%{?!2:%{_infodir}} %{?2}%{?!2:%{_infodir}}/%{1}%ext_info \
%{nil}

%info_del(:-:) test -x /sbin/install-info -a ! -f %{?2}%{?!2:%{_infodir}}/%{1}%ext_info && /sbin/install-info --quiet --delete --info-dir=%{?2}%{?!2:%{_infodir}} %{?2}%{?!2:%{_infodir}}/%{1}%ext_info \
%{nil}

