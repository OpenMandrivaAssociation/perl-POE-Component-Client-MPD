%define upstream_name    POE-Component-Client-MPD
%define upstream_version 1.093390

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    POE component to speak with MPD servers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Audio::MPD::Common::Item)
BuildRequires: perl(Audio::MPD::Common::Stats)
BuildRequires: perl(Audio::MPD::Common::Status)
BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(FindBin)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(MooseX::POE)
BuildRequires: perl(MooseX::SemiAffordanceAccessor)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Component::Client::TCP)
BuildRequires: perl(Readonly)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Corpus::Audio::MPD)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
POCOCM gives a clear message-passing interface (sitting on top of POE) for
talking to and controlling MPD (Music Player Daemon) servers. A connection
to the MPD server is established as soon as a new POCOCM object is created.

Commands are then sent to the server as messages are passed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
