%define DIRNAME test-data
%define LIBNAME smartmet-%{DIRNAME}
%define SPECNAME smartmet-%{DIRNAME}
Summary: Smartmet server static test data
Name: %{SPECNAME}
Version: 19.10.31
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
%{_datadir}/smartmet/test/data/*
%defattr(0775,root,root,0777)
%{_datadir}/smartmet/test/data/sqlite

%changelog
* Thu Oct 31 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.10.31-1.fmi
- Added indexes to sqlite tables
- Removed some observations to keep sqlite data below 100 MB limit

* Thu May  9 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.5.9-1.fmi
- sqlite-directory needs to be writable for temporary files

* Fri Apr 26 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.4.26-1.fmi
- Fixed climate data to be in the original YKJ projection, the stereographic version was projected incorrectly

* Tue Feb 12 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.2.12-1.fmi
- Added forestfire-data for WMS tests

* Wed Jan 30 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.1.30-1.fmi
- Added grassfire-data for WMS tests

* Wed Sep 26 2018 Mika Heiskanen <mika.heiskanen@fmi.fi> - 18.9.26-1.fmi
- Removed extra valgrind files

* Tue Sep 25 2018 Mika Heikki Pernu <heikki.pernu@fmi.fi> - 18.9.25-1.fmi
- Packaged test data as an RPM
