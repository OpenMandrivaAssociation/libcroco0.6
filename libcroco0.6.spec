%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname libcroco
%define api 0.6
%define major 3
%define libname %mklibname croco %{api} %{major}
%define devname %mklibname croco %{api} -d

Summary:	CSS2 parser library
Name:		%{oname}%{api}
Version:	0.6.12
Release:	1
License:	LGPLv2
Group:		System/Libraries
Url:		http://savannah.nongnu.org/projects/libcroco
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
libcroco is a standalone css2 parsing library.
It provides a low level event driven SAC like api
and a css object model like api.

%package -n %{libname}
Summary:	CSS2 parser library
Group:		System/Libraries

%description -n %{libname}
libcroco is a standalone css2 parsing library.
It provides a low level event driven SAC like api
and a css object model like api.

%package -n %{devname}
Summary:	Libraries and include files for developing with libcroco
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname croco0.6_3 -d} < 0.6.5

%description -n %{devname}
This package provides the necessary development libraries and include
files to allow you to develop with libcroco?

%package utils
Summary:	Example apps based on libcroco for working with CSS files
Group:		Text tools

%description utils
This contains the example apps that come with libcroco. At the moment this is
csslint, a Cascading Style Sheets checker.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/croco-%{api}-config

%files utils
%doc README AUTHORS COPYING COPYING.LIB ChangeLog NEWS
%{_bindir}/csslint-%{api}

%files -n %{libname}
%{_libdir}/libcroco-%{api}.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/libcroco/
%{_bindir}/croco-%{api}-config
%{multiarch_bindir}/croco-%{api}-config
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

