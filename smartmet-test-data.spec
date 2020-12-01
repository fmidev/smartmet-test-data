%define DIRNAME test-data
%define LIBNAME smartmet-%{DIRNAME}
%define SPECNAME smartmet-%{DIRNAME}
Summary: Smartmet server static test data
Name: %{SPECNAME}
Version: 20.12.1
Release: 3%{?dist}.fmi
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
* Tue Dec  1 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.12.1-3.fmi
- Added many t2m, wpsd and wdir observations for 20130805T1500 for WMS tests

* Tue Dec  1 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.12.1-2.fmi
- Removed obsolete test-data whose time range is entirely covered by another data

* Mon Nov 30 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.11.30-1.fmi
- Added new data from Helsinki area to make new TimeSeries distance search tests pass

* Mon Nov 23 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.11.23-1.fmi
- Fixed stations.txt file, it had wrong dates for example for Kaisaniemi AWS

* Tue Nov 10 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.11.10-1.fmi
- sqlite-cache updated, weather_data_qc parameter is now an integer

* Thu Oct 29 2020 Anssi Reponen <anssi.reponen@fmi.fi> - 20.10.29-1.fmi
- Sqlite-file updated because type of timestamp field changed (BRAINSTORM-1950)

* Thu Oct 22 2020 Anssi Reponen <anssi.reponen@fmi.fi> - 20.10.22-1.fmi
- Added sqlite-file for observation tests (BRAINSTORM-1940)

* Thu Oct  1 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.10.1-1.fmi
- Removed obsolete stations subdirectory, use sqlite directory instead

* Tue Jun 30 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.6.30-1.fmi
- Added WRF test data

* Thu Jun 25 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.6.25-1.fmi
- Added GEM test data

* Mon Jun  1 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.6.1-1.fmi
- Added MEPS data with the correct WGS84 datum. Metcoop data is now deprecated.

* Fri May 29 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.5.29-1.fmi
- Fixed metcoop +lat_2 to value 63.3

* Wed May 27 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.5.27-1.fmi
- Replaced old metcoop test data with a deprecated NFmiGdalArea projection with a NFmiLambertConformalConicArea projection

* Fri May 15 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.5.15-1.fmi
- Use ISO timestamp format for all observations (T was missing)

* Wed May 13 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.5.13-1.fmi
- Removed obsolete tables from stations.sqlite and added sensor_no column

* Thu May  7 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.5.7-1.fmi
- Added sample raster data for tests

* Tue Feb 11 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.2.11-1.fmi
- Fixed test sqlite database
- Start using LFS for the sqlite database

* Mon Nov  4 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.11.4-1.fmi
- Fixed the modification time of all querydata files to keep WFS test results the same

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
