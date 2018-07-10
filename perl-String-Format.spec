%define modname	String-Format
%define modver 1.17

Summary:	Sprintf-like string formatting capabilities with arbitrary format definitions 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/String/String-Format-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
String::Format lets you define arbitrary printf-like format sequences to be
expanded. This module would be most useful in configuration files and reporting
tools, where the results of a query need to be formatted in a particular way.
It was inspired by mutt's index_format and related directives (see
<URL:http://www.mutt.org/doc/manual/manual-6.html#index_format>).

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/String
%{_mandir}/man3/*


