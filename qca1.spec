%define rname	qca
Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca1
Version:	1.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://delta.affinix.com/qca/%{rname}-%{version}.tar.bz2
# Source0-md5:	ee44022eb0e5b8b5df64c62630f6e6b6
Patch0:		%{rname}-libs.patch
URL:		http://delta.affinix.com/qca/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qmake
BuildRequires:	qt-devel >= 6:3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Cryptographic Architecture (QCA) Library.

%description -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA).

%package devel
Summary:	Qt Cryptographic Architecture (QCA) Library - development files
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	qt-devel >= 6:3.1.2

%description devel
Qt Cryptographic Architecture (QCA) Library - development files.

%description devel -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla programistów.

%prep
%setup -q -n %{rname}-%{version}
%patch -P0 -p1

%build
export QTDIR=%{_prefix}
export LIBDIR=%{_libdir}

./configure \
	--prefix=%{_prefix} \
# probably could be done but breaks the build now:
#
#qmake %{name}.pro \
#	QMAKE_CXX="%{__cxx}" \
#	QMAKE_LINK="%{__cxx}" \
#	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
#	QMAKE_RPATH=

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/qca.h
