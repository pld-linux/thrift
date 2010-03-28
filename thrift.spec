Summary:	Framework for scalable cross-language services development
Summary(pl.UTF-8):	-
Name:		thrift
Version:	0.2.0
Release:	0.1
License:	- enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
# http://www.apache.net.pl/incubator/thrift/0.2.0-incubating/thrift-0.2.0-incubating.tar.gz
Source0:	http://www.apache.net.pl/incubator/%{name}/%{version}-incubating/%{name}-%{version}-incubating.tar.gz
URL:		http://incubator.apache.org/thrift/
BuildRequires:	-
Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software framework for scalable cross-language services development. It combines a software stack with a code generation engine to build services that work efficiently and seamlessly between C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, Smalltalk, and OCaml.

%description -l pl.UTF-8

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
