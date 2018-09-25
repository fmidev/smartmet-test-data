%define DIRNAME test-data
%define LIBNAME smartmet-%{DIRNAME}
%define SPECNAME smartmet-%{DIRNAME}
Summary: Smartmet server static test data
Name: %{SPECNAME}
Version: 18.9.25
Release: 1%{?dist}.fmi
License: MIT
Group: Development/Libraries
URL: https://github.com/fmidev/smartmet-test-data
Source: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: make
BuildRequires: /usr/bin/install
BuildRequires: rpm-build
#TestRequires: make
Provides: %{LIBNAME}

%description
FMI data used for testing Smartmet server components.
Data is not needed for production.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{SPECNAME}
 
%build
make %{_smp_mflags}

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0775,root,root,0775)
%{_datadir}/smartmet/test/*
%{_bindir}/init_test_data

%changelog
* Tue Sep 25 2018 Mika Heikki Pernu <heikki.pernu@fmi.fi> - 18.9.25-1.fmi
- Packaged test data as an RPM