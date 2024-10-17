Name:		generatorrunner
Version:	0.6.16
Release:	1
License:	GPLv2
Summary:	A utility that parses header and typesystem files
Group:		Development/KDE and Qt
URL:		https://www.pyside.org
Source0:	http://www.pyside.org/files/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	apiextractor-devel >= 0.10.10
Conflicts:	%{_lib}gen0 < 0.3.3
Obsoletes:	boostpythongenerator < 0.6.0

%description
Generator is a utility that parses a collecion of header and typesystem
files, generating other files (code, documentation, etc.) as result.

%files
%{_bindir}/*
%{_libdir}/generatorrunner
%{_mandir}/man1/*.1.*

#------------------------------------------------------------------------------

%define libgen_major 0
%define libgen %mklibname genrunner %{libgen_major}

%package -n %{libgen}
Summary:	Generator core lib
Group:		System/Libraries

%description -n %{libgen}
Generator core lib.

%files -n %{libgen}
%{_libdir}/libgenrunner.so.%{libgen_major}*

#------------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for Generator
Group:		Development/KDE and Qt
Requires:	%{libgen} = %{version}
Requires:	apiextractor-devel >= 0.9.3
Requires:	%{name} = %{version}
Obsoletes:	boostpythongenerator-devel < 0.3.3

%description devel
Devel stuff for Generator.

%files devel
%{_includedir}/*
%{_libdir}/libgenrunner.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%__sed 's/-Wno-strict-aliasing/-fno-strict-aliasing/' -i CMakeLists.txt
%cmake
%make

%install
%makeinstall_std -C build


%changelog
* Sat Apr 07 2012 Andrey Bondrov <abondrov@mandriva.org> 0.6.16-1
+ Revision: 789629
- New version 0.6.16

* Tue Oct 25 2011 Andrey Bondrov <abondrov@mandriva.org> 0.6.14-1
+ Revision: 707122
- New version 0.6.14

* Tue Sep 20 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.12-1
+ Revision: 700469
- update buildrequires version
- new version

* Tue Sep 20 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.11-2
+ Revision: 700442
- clean out obsolete rpm junk
- rebuild

* Thu Jul 14 2011 Lev Givon <lev@mandriva.org> 0.6.11-1
+ Revision: 689945
- Update to 0.6.11.

* Wed Jul 13 2011 Lev Givon <lev@mandriva.org> 0.6.10-3
+ Revision: 689906
- Fix release tag.

* Wed Jun 08 2011 Paulo Belloni <paulo@mandriva.com> 0.6.10-2
+ Revision: 683170
- Fixing no-strict-aliasing flag. We need to inform upstream.

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.6.10-1
+ Revision: 680403
- new version 0.6.10

* Sun May 01 2011 Funda Wang <fwang@mandriva.org> 0.6.9-1
+ Revision: 661157
- new version 0.6.9

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 0.6.8-1
+ Revision: 649941
- update to new version 0.6.8

* Sat Mar 05 2011 Funda Wang <fwang@mandriva.org> 0.6.7-1
+ Revision: 642047
- new version 0.6.7

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.6.6-1
+ Revision: 640579
- new version 0.6.6

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.6.5-2
+ Revision: 640435
- rebuild to obsolete old packages

* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 0.6.5-1
+ Revision: 635747
- new versio 0.6.5

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 0.6.4-1
+ Revision: 633803
- new version 0.6.4

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 0.6.3-1mdv2011.0
+ Revision: 601814
- new version 0.6.3

* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 0.6.2-1mdv2011.0
+ Revision: 585674
- new version 0.6.2

* Wed Sep 22 2010 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 580561
- new version 0.6.1

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 566334
- New version 0.6.0

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.3.3-2mdv2010.1
+ Revision: 500262
- conflicts boostpythongenerator
- obsoletes old libs
- import generatorrunner


