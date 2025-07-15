# TODO
# - python3 interface
# - rename -libs to -cpp, -devel to -cpp-devel, -static to -cpp-static?
# - no SONAME ext in -libs, enforce some?
# - BR for java, ruby, perl, more general BR
# - Separate packages per each language
# - fix perl: missing vendordir on install
# - fix java: not installing to %{_javadir}
# - avoid downloading from net when build building java
# - Fix ruby install
# - Add Mono
# - Fix parallel build make.
# - dart?
#
# TODO (2) - fix or disable
# - java - br, build, files - icedtea7 ?
# - erlang - build, files
# - php_extension - br, build
# - ruby - build, files, some gems required for build?
# - haskell - build, files
# - d - needs working dmd or gdm to build
# - golang
# - rust (>= 1.13)
# - haxe (>= 3.1.3)
#
# Conditional build:
#
# generic options
%bcond_with	tests		# build with tests
#
# language options
%bcond_without	cpp		# build the C++ library
%bcond_with	qt4		# build the Qt4 library
%bcond_with	qt5		# build the Qt5 library
%bcond_without	c_glib		# build the C (GLib) library
%bcond_with	csharp		# build the C# library
%bcond_with	java		# build the Java library
%bcond_with	erlang		# build the Erlang library
%bcond_with	nodejs		# build nodejs library
%bcond_with	lua		# build Lua library
%bcond_without	python		# build the Python library
%bcond_with	perl		# build the Perl library
%bcond_with	php		# build the PHP library
%bcond_with	php_extension	# build the PHP_EXTENSION library
%bcond_with	ruby		# build the Ruby library
%bcond_with	haskell		# build the Haskell library
%bcond_with	go		# build the Go library
%bcond_with	d		# build the D library

%if %{with perl}
%define		pdir	Thrift
%endif

%if 0%{!?php_name:1}
%define		php_name	php72
%endif

%define		php_min_version 5.3.0
Summary:	Framework for scalable cross-language services development
Summary(pl.UTF-8):	Szkielet budowania skalowalnych usług dla różnych języków programowania
Name:		thrift
Version:	0.11.0
Release:	5
License:	Apache v2.0
Group:		Development/Libraries
Source0:	http://www.apache.org/dist/thrift/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0be59730ebce071eceaf6bfdb8d3a20e
Patch0:		no_bundler_use.patch
Patch1:		no_grunt.patch
Patch2:		no_pom.patch
URL:		http://thrift.apache.org/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.13
BuildRequires:	bison >= 2.5
BuildRequires:	boost-devel >= 1.54.0
BuildRequires:	flex
BuildRequires:	libevent-devel >= 1.0
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	zlib-devel >= 1.2.3
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4.3
BuildRequires:	QtNetwork-devel >= 4.3
BuildRequires:	qt4-build >= 4.3
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5.0
BuildRequires:	Qt5Network-devel >= 5.0
BuildRequires:	qt5-build >= 5.0
%endif
%if %{with c_glib}
BuildRequires:	glib2-devel >= 2.0
%endif
%if %{with csharp}
BuildRequires:	mono-csharp >= 2.11.0
BuildRequires:	mono-devel >= 2.11.0
%endif
%if %{with java}
BuildRequires:	ant >= 1.7
BuildRequires:	java-gcj-compat-devel
BuildRequires:	java-ivy
%endif
%if %{with lua}
BuildRequires:	lua52-devel >= 5.2
%endif
%if %{with nodejs}
BuildRequires:	nodejs
BuildRequires:	npm
%endif
%if %{with python}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-twisted
%endif
%if %{with perl}
BuildRequires:	perl-Bit-Vector
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-base
%endif
%if %{with php}
BuildRequires:	%{php_name}-cli
BuildRequires:	%{php_name}-devel
BuildRequires:	phpunit
%endif
%if %{with erlang}
BuildRequires:	erlang
%endif
%if %{with ruby}
BuildRequires:	ruby
BuildRequires:	ruby-bundler
%endif
%if %{with haskell}
BuildRequires:	ghc
BuildRequires:	ghc-haskell-platform
%endif
%if %{with go}
BuildRequires:	golang
%endif
%if %{with d}
BuildRequires:	dmd
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# library use symbols provided by the glib2 libraries
%define         skip_post_check_so      libthrift_c_glib.so.*

%description
The Apache Thrift software framework, for scalable cross-language
services development, combines a software stack with a code generation
engine to build services that work efficiently and seamlessly between
C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa,
JavaScript, Node.js, Smalltalk, OCaml and Delphi and other languages.

%description -l pl.UTF-8
Programowy szkielet dla rozwoju skalowanych usług dla różnych języków
programowania. Zawiera oprogramowanie wraz silnikiem generowania kodu
do tworzenie usług które spawnie działają pomiędzy C++, Javą,
Pythonem, PHP, Rybym, Erlangiem, Perlem, Haskellem, C#, Cocoa,
Smalltalikiem i Ocamlem.

%package libs
Summary:	C++ Thrift interface libraries
Summary(pl.UTF-8):	Interfejs Thrift dla C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description libs
C++ Thrift interface libraries

%description libs -l pl.UTF-8
Biblioteki interfejsu Thrift dla C++.

%package devel
Summary:	C++ Thrift interface header files
Summary(pl.UTF-8):	Pliki nagłówkowe interfejsu C++ Thrift
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for C++ Thrift interface.

%description devel -l pl.UTF-8
Pliki nagłówkowe interfejsu C++ Thrift.

%package static
Summary:	Thrift C++ static libraries
Summary(pl.UTF-8):	Biblioteki statyczne interfejsu C++ Thrift
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library files for C++ Thrift interface.

%description static -l pl.UTF-8
Statyczne biblioteki interfejsu C++ Thrift.

%package -n php-%{name}
Summary:	PHP Thrift interface
Summary(pl.UTF-8):	Interfejs Thrift dla PHP
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php(core) >= %{php_min_version}

%description -n php-%{name}
PHP Thrift interface.

%description -n php-%{name} -l pl.UTF-8
Interfejs Thrift dla PHP.

%package -n python-%{name}
Summary:	Python Thrift interface
Summary(pl.UTF-8):	Interfejs Thrift dla Pythona
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-%{name}
Python Thrift interface.

%description -n python-%{name} -l pl.UTF-8
Interfejs Thrift dla Pythona.

%package -n perl-Thrift
Summary:	Perl Thrift interface
Summary(pl.UTF-8):	Interfejs Thrift dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Thrift
Perl Thrift interface.

%description -n perl-Thrift -l pl.UTF-8
Interfejs Thrift dla Perla.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__aclocal} -I aclocal
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PHP_PREFIX=%{php_data_dir} \
	PHP=%{__php} \
	PERL_PREFIX=%{perl_vendorlib} \
	TRIAL=/usr/bin/trial-2 \
	--enable-libs \
	--disable-tutorial \
	--disable-tests \
	--with-boost \
	%{__with_without c_glib} \
	%{__with_without csharp} \
	%{__with_without cpp} \
	%{__with_without d} \
	%{__with_without erlang} \
	%{__with_without go} \
	%{__with_without java} \
	%{__with_without haskell} \
	--with-libevent \
	%{__with_without lua} \
	%{__with_without nodejs} \
	%{__with_without python} \
	%{__with_without perl} \
	%{__with_without php} \
	%{__with_without php_extension} \
	%{__with_without qt4} \
	%{__with_without qt5} \
	--without-rs \
	%{__with_without ruby} \
	%{__with_without tests} \
	--with-zlib

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif

%if %{with perl}
%{__mv} $RPM_BUILD_ROOT%{perl_vendorlib}/lib/perl5/Thrift{,.pm} $RPM_BUILD_ROOT%{perl_vendorlib}
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/thrift

%if %{with cpp}
%files libs
%defattr(644,root,root,755)
%{_libdir}/libthrift-%{version}.so
%{_libdir}/libthriftnb-%{version}.so
%{_libdir}/libthriftz-%{version}.so
%if %{with qt4}
%{_libdir}/libthriftqt-%{version}.so
%endif
%if %{with qt5}
%{_libdir}/libthriftqt5-%{version}.so
%endif
%if %{with c_glib}
%{_libdir}/libthrift_c_glib.so.*
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/libthrift.so
%{_libdir}/libthriftnb.so
%{_libdir}/libthriftz.so
%{_includedir}/thrift
%{_pkgconfigdir}/thrift-nb.pc
%{_pkgconfigdir}/thrift-z.pc
%{_pkgconfigdir}/thrift.pc
%if %{with qt4}
%{_libdir}/libthriftqt.so
%{_pkgconfigdir}/thrift-qt.pc
%endif
%if %{with qt5}
%{_libdir}/libthriftqt5.so
%{_pkgconfigdir}/thrift-qt5.pc
%endif
%if %{with c_glib}
%{_libdir}/libthrift_c_glib.so
%{_pkgconfigdir}/thrift_c_glib.pc
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/libthrift.a
%{_libdir}/libthriftnb.a
%{_libdir}/libthriftz.a
%if %{with qt4}
%{_libdir}/libthriftqt.a
%endif
%if %{with qt5}
%{_libdir}/libthriftqt5.a
%endif
%if %{with c_glib}
%{_libdir}/libthrift_c_glib.a
%endif
%endif

%if %{with php}
%files -n php-%{name}
%defattr(644,root,root,755)
%{php_data_dir}/Thrift
%endif

%if %{with python}
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
%{py_sitedir}/thrift-%{version}-py*.egg-info
%endif
%endif

%if %{with perl}
%files -n perl-Thrift
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Thrift
%{perl_vendorlib}/Thrift.pm
%{perl_vendorlib}/Thrift/*.pm
%endif
