%define bname   gumbo
%define libname %mklibname gumbo
%define devname %mklibname gumbo -d

Name:		gumbo-parser
Version:	0.14.1
Release:	1
Source0:	https://codeberg.org/gumbo-parser/gumbo-parser/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Gumbo is an implementation of the HTML5 parsing algorithm implemented as a pure C99 library with no outside dependencies
URL:		https://codeberg.org/gumbo-parser/gumbo-parser
License:	Apache-2.0
Group:		Networking/Other

BuildRequires:  pkgconfig(gtest)

BuildSystem:    meson
BuildOption:	-Dpython=true
BuildOption:    -Dcpp_std=c++17

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as a pure C99 library with no outside dependencies. It's designed to serve as a building block for other tools and libraries such as linters, validators, templating languages, and refactoring and analysis tools.

%package -n python-%{bname}
Summary:	Python bindings for gumbo-parser
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
Requires:	%{libname}
%description -n python-%{bname}
Python bindings for gumbo-parser

%install -a
%libpackages
echo %{_includedir}/tag_enum.h >>%{specpartsdir}/%{mklibname -d gumbo}.specpart
echo %{_includedir}/%{bname}.h >>%{specpartsdir}/%{mklibname -d gumbo}.specpart

%files -n python-%{bname}
%{py_sitedir}/%{bname}
