%define upstream_name    Class-Field
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Class Field Accessor Generator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Filter::Util::Call)
BuildArch:	noarch

%description
Class::Field exports two subroutines, 'field' and 'const'. These functions
are used to declare fields and constants in your class.

Class::Field generates custom code for each accessor that is optimized for
speed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.150.0-2mdv2011.0
+ Revision: 654892
- rebuild for updated spec-helper

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 399313
- import perl-Class-Field


* Fri Jul 24 2009 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist
