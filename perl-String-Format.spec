%define upstream_name    String-Format
%define upstream_version 1.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Sprintf-like string formatting capabilities with arbitrary format definitions 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
String::Format lets you define arbitrary printf-like format sequences to be
expanded. This module would be most useful in configuration files and reporting
tools, where the results of a query need to be formatted in a particular way.
It was inspired by mutt's index_format and related directives (see
<URL:http://www.mutt.org/doc/manual/manual-6.html#index_format>).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/String
%{_mandir}/*/*
