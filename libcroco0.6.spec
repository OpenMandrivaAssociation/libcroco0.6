# libcroco0.6 is used by librsvg, librsvg is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname libcroco
%define api 0.6
%define major 3
%define libname %mklibname croco %{api} %{major}
%define devname %mklibname croco %{api} -d
%define lib32name %mklib32name croco %{api} %{major}
%define dev32name %mklib32name croco %{api} -d

Summary:	CSS2 parser library
Name:		%{oname}%{api}
Version:	0.6.13
Release:	4
License:	LGPLv2
Group:		System/Libraries
Url:		http://savannah.nongnu.org/projects/libcroco
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libcroco/%{url_ver}/%{oname}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(icu-i18n)
%if %{with compat32}
BuildRequires:	devel(libglib-2.0)
BuildRequires:	devel(libxml2)
BuildRequires:	devel(libz)
BuildRequires:	devel(libbz2)
BuildRequires:	devel(libffi)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	CSS2 parser library (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
libcroco is a standalone css2 parsing library.
It provides a low level event driven SAC like api
and a css object model like api.

%package -n %{dev32name}
Summary:	Libraries and include files for developing with libcroco (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package provides the necessary development libraries and include
files to allow you to develop with libcroco?
%endif

%prep
%autosetup -n %{oname}-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files utils
%doc README AUTHORS COPYING COPYING.LIB ChangeLog NEWS
%{_bindir}/csslint-%{api}

%files -n %{libname}
%{_libdir}/libcroco-%{api}.so.%{major}*

%files -n %{devname}
%optional %doc %{_datadir}/gtk-doc/html/libcroco/
%{_bindir}/croco-%{api}-config
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libcroco-%{api}.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*
%endif
