Name: generatorrunner
Version: 0.3.3
Release: %mkrel 1
License: GPLv2
Summary: A utility that parses header and typesystem files
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0:  http://www.pyside.org/files/%name-%version.tar.bz2
Patch0: generatorrunner-0.3.3-cmake-install-module.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: boost-devel
BuildRequires: apiextractor-devel >= 0.3.3
BuildRequires: openssl-devel

%description
Generator is a utility that parses a collecion of header and typesystem
files, generating other files (code, documentation, etc.) as result.

%files 
%defattr(-,root,root,-)
%_bindir/*
%{_libdir}/generatorrunner
%{_mandir}/man1/*.1.*

#------------------------------------------------------------------------------

%define libgen_major 0
%define libgen %mklibname genrunner %{libgen_major}

%package -n %{libgen}
Summary: boostpythongenerator core lib
Group: System/Libraries

%description -n %{libgen}
Boostpythongenerator core lib.

%files -n %{libgen}
%defattr(-,root,root)
%{_libdir}/libgenrunner.so.%{libgen_major}*

#------------------------------------------------------------------------------

%package devel
Summary: Devel stuff for boostpythongenerator
Group: Development/KDE and Qt
Requires: %{libgen} = %{version}
Requires: apiextractor-devel >= 0.3
Requires: %name = %{version}

%description devel
Devel stuff for boostpythongenerator.

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libgenrunner.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/Modules/*

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .install

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %buildroot

