%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname elasticsearch-py

Name:		python-elasticsearch
Version:	1.2.0
Release:	3%{?dist}
Summary:	Python client for Elasticsearch

Group:		Development/Libraries
License:	Apache
URL:		https://github.com/elasticsearch/elasticsearch-py
Source0:	https://github.com/elasticsearch/elasticsearch-py/archive/%{version}.tar.gz
Patch0:     https://raw.github.com/mwhahaha/rpm-%{name}/master/%{srcname}-1.2.0-urllib.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python-setuptools
Requires:       python-unittest2

%description
Official low-level client for Elasticsearch. It's goal is to provide common
ground for all Elasticsearch-related code in Python; because of this it tries
to be opinion-free and very extendable.


%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
rm -rf %{buildroot}
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{python2_sitelib}/elasticsearch-%{version}-py*.egg-info/*
%{python2_sitelib}/elasticsearch/*


%changelog
* Thu Oct 30 2014 Alex Schultz <aschultz@next-development.com> 1.2.0-3
- Updates to the spec file
* Tue Aug 12 2014 Matt Dainty <matt@bodgit-n-scarper.com> 1.2.0-2
- Update dependencies, patch urllib requirement back down.
* Tue Aug 12 2014 Matt Dainty <matt@bodgit-n-scarper.com> 1.2.0-1
- Bump to 1.2.0.
* Mon Jun 23 2014 Matt Dainty <matt@bodgit-n-scarper.com> 1.0.0-1
- Initial build.
