%define oname libcroco
%define majorminor 0.6
%define lib_major 3
%define lib_name %mklibname croco%{majorminor}_ %{lib_major}
%define develname %mklibname croco%{majorminor} -d

Name:		%{oname}%{majorminor}
Summary:	CSS2 parser library
Version: 	0.6.3
Release:	1
License: 	LGPLv2
Group:		System/Libraries
URL: 		http://savannah.nongnu.org/projects/libcroco
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.xz
Patch0:		libcroco-0.6.2-format-strings.patch

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)

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

%package -n %{develname}
Summary:	Libraries and include files for developing with libcroco
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname croco%{majorminor}_ %{lib_major} -d

%description -n %{develname}
This package provides the necessary development libraries and include
files to allow you to develop with libcroco?

%package utils
Summary: Example apps based on libcroco for working with CSS files
Group:	Text tools

%description utils
This contains the example apps that come with libcroco. At the moment this is
csslint, a Cascading Style Sheets checker.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build

%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unpackaged files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%multiarch_binaries %{buildroot}%{_bindir}/croco-%{majorminor}-config

%files utils
%doc README AUTHORS COPYING COPYING.LIB ChangeLog NEWS
%{_bindir}/csslint-%{majorminor}

%files -n %{lib_name}
%{_libdir}/*.so.%{lib_major}*

%files -n %{develname}
%{_bindir}/croco-%{majorminor}-config
%{multiarch_bindir}/croco-%{majorminor}-config
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%doc %{_datadir}/gtk-doc/html/libcroco/

