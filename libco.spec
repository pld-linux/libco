Summary:	Cooperative multithreading library
Name:		libco
Version:	20
Release:	1
License:	ISC
Group:		Libraries
Source0:	https://github.com/canonical/libco/archive/v%{version}.tar.gz
# Source0-md5:	c1c2107b7ffbd26645b8a7d188e5813b
URL:		https://github.com/canonical/libco
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For applications that need 100,000 or more context switches per
second, the kernel overhead involved in preemptive multithreading can
end up becoming the bottleneck in the application. libco can easily
scale to 10,000,000 or more context switches per second.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development files for the %{name} library.

%package static
Summary:	Static libraries for %{name} development
Summary(pl.UTF-8):	Statyczne biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static %{name} library.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=$(basename %{_libdir})

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libco.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libco.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libco.so
%{_includedir}/libco.h
%{_pkgconfigdir}/libco.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libco.a
