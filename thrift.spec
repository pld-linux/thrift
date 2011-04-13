# TODO
# - BR for java, ruby, perl, more general BR
# - Separate packages per each language
# - fix perl: missing vendordir on install
# - fix java: not installing to %{_javadir}
# - avoid downloading from net when build building java
# - Fix ruby install
# - Fix PHP build
# - Add Mono
# - Fix parallel build make.

Summary:	Framework for scalable cross-language services development
Summary(pl.UTF-8):	Szkielet budowania skalowalnych usług dla różnych języków programowania
Name:		thrift
Version:	0.5.0
Release:	3.9
License:	Apache v2.0
Group:		Development/Libraries
Source0:	http://ftp.tpnet.pl/vol/d1/apache//incubator/thrift/%{version}-incubating/%{name}-%{version}.tar.gz
# Source0-md5:	14c97adefb4efc209285f63b4c7f51f2
Patch0:		%{name}-Werror_strlcpy_fix.patch
Patch1:		%{name}-cpp_link_fix.patch
URL:		http://incubator.apache.org/thrift/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	flex
BuildRequires:	libevent-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	zlib-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software framework for scalable cross-language services development.
It combines a software stack with a code generation engine to build
services that work efficiently and seamlessly between C++, Java,
Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, Smalltalk, and
OCaml.

%description -l pl.UTF-8
Programowy szkielet dla rozwoju skalowanych usług dla różnych języków
programowania. Zawiera oprogramowanie wraz silnikiem generowania kodu
do tworzenie usług które spawnie działają pomiędzy C++, Javą,
Pythonem, PHP, Rybym, Erlangiem, Perlem, Haskellem, C#, Cocoa,
Smalltalikiem i Ocamlem.


%package devel
Summary:	C++ header files
Summary(pl.UTF-8):	Pliki nagłówkowe i bibliotek iterfejsu C++ thrift
Group:		Development/Libraries
Requires:	%{name}-cpp = %{version}-%{release}

%description devel
Header and libarary files for C++ thrift inteface.

%description devel -l pl.UTF-8
Pliki nagłówkowe i bibliotek iterfejsu C++ thrift.


%package static
Summary:	Thrift C++ static libraries
Summary(pl.UTF-8):	Biblioteki statyczne iterfejsu C++ thrift
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libarary files for C++ thrift inteface.

%description static -l pl.UTF-8
Statyczne biblioteki iterfejsu C++ thrift.


%package -n %{name}-libs
Summary:	C++ thrift interface libraries
Summary(pl.UTF-8):	Interfejs thrift dla C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{name}-libs
C++ thrift interface libraries

%description -n %{name}-libs -l pl.UTF-8
Biblioteki interfejsu thrift dla C++.


%package -n python-%{name}
Summary:	Python thrift interface
Summary(pl.UTF-8):	Interfejs thrift dla Pythona
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-%{name}
Python thrift interface.

%description -n python-%{name} -l pl.UTF-8
Interfejs thrift dla Pythona.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# %{__aclocal}
# %{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-csharp \
	--without-erlang \
	--without-haskell \
	--without-java \
	--without-perl \
	--without-php \
	--without-php_extension \
	--without-ruby

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/thrift

%files devel
%defattr(644,root,root,755)
%{_libdir}/libthrift.la
%{_libdir}/libthriftz.la
%{_libdir}/libthriftnb.la
%attr(755,root,root) %{_libdir}/libthrift.so
%attr(755,root,root) %{_libdir}/libthriftz.so
%attr(755,root,root) %{_libdir}/libthriftnb.so
%{_includedir}/%{name}
%{_pkgconfigdir}/thrift-nb.pc
%{_pkgconfigdir}/thrift-z.pc
%{_pkgconfigdir}/thrift.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libthrift.a
%{_libdir}/libthriftz.a
%{_libdir}/libthriftnb.a

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libthrift.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libthrift.so.0
%attr(755,root,root) %{_libdir}/libthriftz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libthriftz.so.0
%attr(755,root,root) %{_libdir}/libthriftnb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libthriftnb.so.0

%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{name}
%dir %{py_sitedir}/%{name}/protocol
%{py_sitedir}/%{name}/protocol/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{name}/protocol/fastbinary.so
%dir %{py_sitedir}/%{name}/server
%{py_sitedir}/%{name}/server/*.py[co]
%dir %{py_sitedir}/%{name}/transport
%{py_sitedir}/%{name}/transport/*.py[co]
%{py_sitedir}/%{name}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/Thrift-*.egg-info
%endif
