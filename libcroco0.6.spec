%define oname libcroco
%define majorminor 0.6
%define name %oname%majorminor
%define lib_major 3
%define lib_name %mklibname croco%{majorminor}_ %{lib_major}

Name:		%name
Summary:	CSS2 parser library
Version: 	0.6.1
Release: %mkrel 3
License: 	LGPL
Group:		System/Libraries
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
URL: 		http://savannah.nongnu.org/projects/libcroco
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libxml2-devel
BuildRequires:  pango-devel
BuildRequires:  libgnomeui2-devel

%description
libcroco is a standalone css2 parsing library.
It provides a low level event driven SAC like api
and a css object model like api.

%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}

%description -n %{lib_name}
libcroco is a standalone css2 parsing library.
It provides a low level event driven SAC like api
and a css object model like api.

%package -n %{lib_name}-devel
Summary:	Libraries and include files for developing with libcroco
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
Provides:   libcroco%majorminor-devel = %{version}-%{release}
Requires:	libxml2-devel
Requires:	libglib2-devel

%description -n %{lib_name}-devel
This package provides the necessary development libraries and include
files to allow you to develop with libcroco?

%package utils
Summary: Example apps based on libcroco for working with CSS files
Group:	Text tools

%description utils
This contains the example apps that come with libcroco. At the moment this is
csslint, a Cascading Style Sheets checker.

%prep
%setup -q -n %oname-%version

%build

%configure2_5x

%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%multiarch_binaries %buildroot%_bindir/croco-%majorminor-config

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig -n %{lib_name}

%postun -p /sbin/ldconfig -n %{lib_name}

%files utils
%defattr(-, root, root)
%doc README
%{_bindir}/csslint-%majorminor

%files -n %{lib_name}
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_bindir}/croco-%majorminor-config
%multiarch_bindir/croco-%majorminor-config
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*


