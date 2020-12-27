Summary:	Cooperative multithreading library
Summary(pl.UTF-8):	Biblioteka wątków kooperatywnych
Name:		libco
Version:	20
Release:	2
License:	ISC
Group:		Libraries
# FIXME: 404
Source0:	https://github.com/canonical/libco/archive/v%{version}.tar.gz
# Source0-md5:	c1c2107b7ffbd26645b8a7d188e5813b
# FIXME: 404
URL:		https://github.com/canonical/libco
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For applications that need 100,000 or more context switches per
second, the kernel overhead involved in preemptive multithreading can
end up becoming the bottleneck in the application. libco can easily
scale to 10,000,000 or more context switches per second.

%description -l pl.UTF-8
Dla aplikacji wymagających 100 000 lub więcej przełączeń kontekstu na
sekundę narzut jądra związany z wielowątkowością wywłaszczaną może być
wąskim gardłem. libco potrafi łatwo skalować się do 10 000 000 lub
większej liczby przełączeń kontekstu na sekundę.

%package devel
Summary:	Header files for libco development
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libco
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development files for the libco library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libco.

%package static
Summary:	Static libco library
Summary(pl.UTF-8):	Statyczna biblioteka libco
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libco library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę libco.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
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
