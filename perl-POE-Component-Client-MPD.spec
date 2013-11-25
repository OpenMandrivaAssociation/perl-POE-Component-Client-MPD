%define upstream_name    POE-Component-Client-MPD
%define upstream_version 1.121670

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	POE component to speak with MPD servers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/POE-Component-Client-MPD-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Audio::MPD::Common::Item)
BuildRequires:	perl(Audio::MPD::Common::Stats)
BuildRequires:	perl(Audio::MPD::Common::Status)
BuildRequires:	perl(Carp)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(MooseX::POE)
BuildRequires:	perl(MooseX::SemiAffordanceAccessor)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Component::Client::TCP)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Corpus::Audio::MPD)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
POCOCM gives a clear message-passing interface (sitting on top of POE) for
talking to and controlling MPD (Music Player Daemon) servers. A connection
to the MPD server is established as soon as a new POCOCM object is created.

Commands are then sent to the server as messages are passed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.100.430-2mdv2011.0
+ Revision: 655427
- add br
- rebuild for updated spec-helper

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.430-1mdv2011.0
+ Revision: 505270
- update to 1.100430

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.390-1mdv2010.1
+ Revision: 474075
- update to 1.093390

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.320-1mdv2010.1
+ Revision: 471073
- adding missing buildrequires:
- import perl-POE-Component-Client-MPD


* Sun Nov 29 2009 cpan2dist 1.093320-1mdv
- initial mdv release, generated with cpan2dist

