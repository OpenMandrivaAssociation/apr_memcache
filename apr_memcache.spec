%define major 0
%define libname	%mklibname %{name} %{major}

Summary:	A client for memcached 
Name:		apr_memcache
Version:	0.7.0
Release:	%mkrel 9
License:	Apache License
Group:          System/Libraries
URL:		http://www.outoforder.cc/projects/libs/apr_memcache/
Source0:	http://www.outoforder.cc/downloads/apr_memcache/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	automake1.9
BuildRequires:	libtool
BuildRequires:	apr-devel >= 1.2.2
BuildRequires:	apr-util-devel >= 1.2.2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
apr_memcache is a client for memcached written in C, using APR and APR-Util. It
provides pooled client connections and is thread safe, making it perfect for
use inside Apache Modules. 

%package -n	%{libname}
Summary:	A client for memcached 
Group: 		System/Libraries

%description -n	%{libname}
apr_memcache is a client for memcached written in C, using APR and APR-Util. It
provides pooled client connections and is thread safe, making it perfect for
use inside Apache Modules. 

%package -n	%{libname}-devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}
Provides:	%{name}-devel = %{version}
Obsoletes:	lib%{name}-devel %{name}-devel

%description -n	%{libname}-devel
apr_memcache is a client for memcached written in C, using APR and APR-Util. It
provides pooled client connections and is thread safe, making it perfect for
use inside Apache Modules.

This package contains development files for %{name}.

%prep

%setup -q

%build
%if %mdkversion >= 200710
export CFLAGS="%{optflags} -fstack-protector"
export CXXFLAGS="%{optflags} -fstack-protector"
export FFLAGS="%{optflags} -fstack-protector"
%endif

#export WANT_AUTOCONF_2_5=1
#rm -f configure
#libtoolize --force --copy && aclocal-1.7 -I m4 && autoheader && automake-1.7 --add-missing --copy --foreign && autoconf

sh ./autogen.sh

#%%configure2_5x \
#    --enable-shared \
#    --enable-static \	      
#    --with-apr=%{_bindir}/apr-config \
#    --with-apr-util=%{_bindir}/apu-config

./configure \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_datadir} \
    --includedir=%{_includedir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_sharedstatedir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --enable-shared \
    --enable-static \
    --with-apr=%{_bindir}/apr-1-config \
    --with-apr-util=%{_bindir}/apu-1-config
			      
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc LICENSE NOTICE test
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root,-)
%dir %{_includedir}/apr_memcache-%{major}
%{_includedir}/apr_memcache-%{major}/*
%{_libdir}/lib*.*a
%{_libdir}/lib*.so
