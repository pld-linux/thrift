# TODO
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
#
# TODO (2) - fix or disable
# - java - br, build, files - icedtea7 ?
# - erlang - build, files
# - php_extension - br, build
# - ruby - build, files, some gems required for build?
# - haskell - build, files
# - d - needs working dmd or gdm to build
#
# Conditional build:
#
# generic options
%bcond_with	tests		# build with tests
#
# language options
%bcond_without	cpp		# build the C++ library
%bcond_without	qt4		# build the Qt library
%bcond_without	c_glib		# build the C (GLib) library
%bcond_without	csharp		# build the C# library
%bcond_with	java		# build the Java library
%bcond_with	erlang		# build the Erlang library
%bcond_without	python		# build the Python library
%bcond_without	perl		# build the Perl library
%bcond_without	php 		# build the PHP library
%bcond_with	php_extension	# build the PHP_EXTENSION library
%bcond_with	ruby		# build the Ruby library
%bcond_with	haskell		# build the Haskell library
%bcond_without	go		# build the Go library
%bcond_with	d		# build the D library

%include	/usr/lib/rpm/macros.perl

%define		php_min_version 5.3.0
Summary:	Framework for scalable cross-language services development
Summary(pl.UTF-8):	Szkielet budowania skalowalnych usług dla różnych języków programowania
Name:		thrift
Version:	0.9.1
Release:	0.4
License:	Apache v2.0
Group:		Development/Libraries
Source0:	http://www.apache.org/dist/thrift/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d2e46148f6e800a9492dbd848c66ab6e
Patch0:		%{name}-Werror_strlcpy_fix.patch
Patch1:		%{name}-cpp_link_fix.patch
URL:		http://thrift.apache.org/
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
%if %{with qt4}
BuildRequires:	QtNetwork-devel
%endif
%if %{with c_glib}
BuildRequires:	glib2-devel
%endif
%if %{with csharp}
BuildRequires:	mono-devel
BuildRequires:	mono-csharp
%endif
%if %{with java}
BuildRequires:	java-gcj-compat-devel
BuildRequires:	java-ivy
%endif
%if %{with python}
BuildRequires:	python
BuildRequires:	python-TwistedCore
%endif
%if %{with perl}
BuildRequires:	perl-base
BuildRequires:	perl-Bit-Vector
%endif
%if %{with php}
BuildRequires:	php-devel
BuildRequires:	php-program
BuildRequires:	php-phpunit-PHPUnit
%endif
%if %{with erlang}
BuildRequires:	erlang
%endif
%if %{with ruby}
BuildRequires:	ruby
BuildRequires:	ruby-rake
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

%package devel
Summary:	C++ header files
Summary(pl.UTF-8):	Pliki nagłówkowe i bibliotek iterfejsu C++ thrift
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

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

%package libs
Summary:	C++ thrift interface libraries
Summary(pl.UTF-8):	Interfejs thrift dla C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description libs
C++ thrift interface libraries

%description libs -l pl.UTF-8
Biblioteki interfejsu thrift dla C++.

%package -n php-%{name}
Summary:	PHP Thrift interface
Summary(pl.UTF-8):	Interfejs Thrift dla PHP
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php(core) >= %{php_min_version}

%description -n php-%{name}
PHP Thrift interface.

%package -n python-%{name}
Summary:	Python thrift interface
Summary(pl.UTF-8):	Interfejs thrift dla Pythona
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-%{name}
Python thrift interface.

%description -n python-%{name} -l pl.UTF-8
Interfejs thrift dla Pythona.

%package -n perl-Thrift
Summary:	Perl thrift interface
Summary(pl.UTF-8):	Interfejs thrift dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Thrift
Perl thrift interface.

%description -n perl-Thrift -l pl.UTF-8
Interfejs thrift dla Perla.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build
%{__aclocal} -I aclocal
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PHP_PREFIX=%{php_data_dir} \
	PERL_PREFIX=%{perl_vendorlib} \
	%{__with_without cpp} \
	%{__with_without qt4} \
	%{__with_without c_glib} \
	%{__with_without csharp} \
	%{__with_without java} \
	%{__with_without erlang} \
	%{__with_without python} \
	%{__with_without bcond_without} \
	%{__with_without perl} \
	%{__with_without php} \
	%{__with_without php_extension} \
	%{__with_without ruby} \
	%{__with_without haskell} \
	%{__with_without go} \
	%{__with_without d} \
	--with-boost \
	--with-libevent \
	--with-zlib \
	%{__with_without tests}

%{__make} -j1 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%if %{with perl}
%{__mv} $RPM_BUILD_ROOT%{perl_vendorlib}/lib/perl5/Thrift{,.pm} $RPM_BUILD_ROOT%{perl_vendorlib}
%endif

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
%if %{with c_glib}
%{_libdir}/libthrift_c_glib.so.*
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/libthrift.la
%{_libdir}/libthriftnb.la
%{_libdir}/libthriftz.la
%{_libdir}/libthrift.so
%{_libdir}/libthriftnb.so
%{_libdir}/libthriftz.so
%{_includedir}/thrift
%{_pkgconfigdir}/thrift-nb.pc
%{_pkgconfigdir}/thrift-z.pc
%{_pkgconfigdir}/thrift.pc
%if %{with qt4}
%{_libdir}/libthriftqt.so
%{_libdir}/libthriftqt.la
%{_pkgconfigdir}/thrift-qt.pc
%endif
%if %{with c_glib}
%{_libdir}/libthrift_c_glib.so
%{_libdir}/libthrift_c_glib.la
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
