%define upstream_name    String-Format
%define upstream_version 1.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Sprintf-like string formatting capabilities with arbitrary format definitions 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
String::Format lets you define arbitrary printf-like format sequences to be
expanded. This module would be most useful in configuration files and reporting
tools, where the results of a query need to be formatted in a particular way.
It was inspired by mutt's index_format and related directives (see
<URL:http://www.mutt.org/doc/manual/manual-6.html#index_format>).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.160.0-4mdv2012.0
+ Revision: 765659
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.160.0-3
+ Revision: 764170
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.160.0-2
+ Revision: 676638
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.0
+ Revision: 404416
- rebuild using %%perl_convert_version

* Tue May 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2010.0
+ Revision: 377816
- update to new version 1.16

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2010.0
+ Revision: 370180
- update to new version 1.15

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.14-5mdv2009.0
+ Revision: 241907
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-3mdv2008.0
+ Revision: 86922
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-2mdv2007.0
- Rebuild

* Thu Dec 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdk
- New release 1.14

* Thu Nov 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdk
- first mdk release

