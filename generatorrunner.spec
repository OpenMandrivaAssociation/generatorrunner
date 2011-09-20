Name: generatorrunner
Version: 0.6.12
Release: 1
License: GPLv2
Summary: A utility that parses header and typesystem files
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0:  http://www.pyside.org/files/%name-%version.tar.bz2
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: apiextractor-devel >= 0.10.6
Conflicts: %{_lib}gen0 < 0.3.3
Obsoletes: boostpythongenerator < 0.6.0

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
Summary: Generator core lib
Group: System/Libraries

%description -n %{libgen}
Generator core lib.

%files -n %{libgen}
%{_libdir}/libgenrunner.so.%{libgen_major}*

#------------------------------------------------------------------------------

%package devel
Summary: Devel stuff for Generator
Group: Development/KDE and Qt
Requires: %{libgen} = %{version}
Requires: apiextractor-devel >= 0.9.3
Requires: %name = %{version}
Obsoletes: boostpythongenerator-devel < 0.3.3

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
sed 's/-Wno-strict-aliasing/-fno-strict-aliasing/' -i CMakeLists.txt
%cmake
%make

%install
%makeinstall_std -C build
