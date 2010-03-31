# TODO
# - BR for java, ruby, perl, more general BR
# - package -libs & ldconfig
# - Separate packages per each lang
# - fix perl: missing vendordir on install
# - fix java: not installing to %{_javadir}
# - Fix ruby install
# - Add Mono
# - avoid downloading from net when build building java
# - libthriftnb.so lacks some libs when linking
Summary:	Framework for scalable cross-language services development
Summary(pl.UTF-8):	Szkielet budowania skalowalnych usług dla różnych języków programowania
Name:		thrift
Version:	0.2.0
Release:	0.2
License:	Apache v2.0
Group:		Development/Libraries
# http://www.apache.net.pl/incubator/thrift/0.2.0-incubating/thrift-0.2.0-incubating.tar.gz
Source0:	http://www.apache.net.pl/incubator/thrift/%{version}-incubating/%{name}-%{version}-incubating.tar.gz
# Source0-md5:	9958c57c402c02171ba0bcc96183505c
Patch0:		%{name}-Werror_strlcpy_fix.patch
URL:		http://incubator.apache.org/thrift/
BuildRequires:	boost-devel >= 1.33.1
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
Pythonem, PHP, Rybym, Erlangiem, Perlem, Heskellem, C#, Cocoa,
Smalltalikiem i Ocamlem.

%package devel
Summary:	Header files for thrift
Summary(pl.UTF-8):	Pliki nagłówkowe thrift
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for thrift.

%description devel -l pl.UTF-8
Pliki nagłówkowe thrift.

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

%build
%configure \
	--without-ruby
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/thrift

%files devel
%defattr(644,root,root,755)
%{_libdir}/libthrift.so
%{_libdir}/libthrift.la
%{_libdir}/libthriftz.so
%{_libdir}/libthriftz.la
%{_includedir}/%{name}
%{_pkgconfigdir}/thrift-nb.pc
%{_pkgconfigdir}/thrift-z.pc
%{_pkgconfigdir}/thrift.pc

%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitedir}
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
