# TODO: BR for java, ruby, perl, more general BR
# TODO: Separate packages per each lang ?
# TODO: Fix ruby install
Summary:	Framework for scalable cross-language services development
Summary(pl.UTF-8):	Szkielet budowania skalowalnych usług dla różnych języków programowania 
Name:		thrift
Version:	0.2.0
Release:	0.1
License:	- enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
# http://www.apache.net.pl/incubator/thrift/0.2.0-incubating/thrift-0.2.0-incubating.tar.gz
Source0:	http://www.apache.net.pl/incubator/%{name}/%{version}-incubating/%{name}-%{version}-incubating.tar.gz
# Source0-md5:	9958c57c402c02171ba0bcc96183505c
Patch0:         %{name}-Werror_strlcpy_fix.patch
URL:		http://incubator.apache.org/thrift/
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	python-devel >= 2.4
BuildRequires:	zlib-devel >= 1.2.3
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software framework for scalable cross-language services development. It combines a software stack with a code generation engine to build services that work efficiently and seamlessly between C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, Smalltalk, and OCaml.

%description -l pl.UTF-8
Programowy szkielet dla rozwoju skalowanych usług dla różnych języków programowania. Zawiera oprogramowanie wraz silnikiem generowania kodu do tworzenie usług
które spawnie działają pomiędzy C++, Javą, Pythonem, PHP, Rybym, Erlangiem, Perlem, Heskellem, C#, Cocoa, Smalltalikiem i Ocamlem.  

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
