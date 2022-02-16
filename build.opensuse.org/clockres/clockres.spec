Name:           clockres
Version:        0.1
Release:        1
Summary:        Dump various clock resolutions for clock_gettime(2) calls

Group:          Development Tools
License:        MIT
URL:            https://github.com/hpaluch-pil/clockres
# NOTE: Must have .tar.gz suffix to work properly with Tito builder
Source0:        %{name}-%{version}.tar.xz
#BuildArch:      x86_64

BuildRequires:  gcc make
%if 0%{?suse_version}
BuildRequires: cmake >= 3.0 cmake-full >= 3.0
%else
# fallback for CentOS 7 and possible others
BuildRequires: cmake3
%endif
%description
Provides simple utility 'clockres' that dumps clock resolutions
for clock_gettime(2) calls. The resolution is gathered using
clock_getres(2) calls.

%prep
%setup -q 

%build
%if 0%{?suse_version}
%cmake .
%cmake_build
%else
%cmake3 .
%cmake3_build
%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}

%if 0%{?suse_version}
%cmake_install
%else
%cmake3_install
%endif


%files
%license LICENSE
%{_bindir}/%{name}

# use  date  '+%a %b %d %Y' to get date in format:
%changelog
