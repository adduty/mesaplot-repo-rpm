Name: mesaplot-repo
Version: 7
Release:	1%{?dist}
Summary: Installs MESAplot repository

Group: System Environment/Base
License: GPLv2
URL: http://mleewise.com/mesaplot.php
Source0: http://mleewise.com/mesaplot/rpm/RPM-GPG-KEY-MESAPLOT-7
Source1: mesaplot.repo

BuildArch: noarch

BuildRequires:	
Requires:	

%description
This package contains the MESAplot repository
GPG key as well as configuration for yum.


%prep
%setup -q
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-MESAPLOT-7

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-MESAPLOT-7

%changelog

* Thu Jun 16 2016 Andrew Duty <tisbeok@gmail.com> 7-1
- Initial package for MESAplot repo.
