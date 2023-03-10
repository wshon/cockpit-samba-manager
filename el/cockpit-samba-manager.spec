Name:           cockpit-samba-manager
Version:        1.0.6
Release:        1%{?dist}
Summary:        A Cockpit plugin to make managing SMB shares easy.
License:        GPL-3.0+
URL:            github.com/45drives/cockpit-samba-manager/blob/main/README.md
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       cockpit samba

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Cockpit Samba Manager
A Cockpit plugin to make managing SMB shares easy.

%prep
%setup -q

%build
# empty

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
cp -a * %{buildroot}

%clean
rm -rf %{buildroot}

%files
/usr/share/cockpit/samba-manager/*

%changelog
* Sun Feb 12 2023 wshon <me@wshon.com> 1.0.7-1
- Fix CSS for Cockpit 273 and greater.

* Wed May 12 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.6-1
- Fix bug where users and shares are duplicated in lists on editing global.

* Wed May 12 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.5-1
- Clear loading spinner on error. Before, the error was obscured.

* Thu Apr 08 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.4-1
- Remove triggering the modals to close on clicking outside of dialog.
- Clear warning message in Global Settings dialog when reopened.
- Exclude domain users and groups from User Management and Share Management,
  only keeping them in the dropdown lists to add to shares.

* Wed Apr 07 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.3-1
- Fix multiple Javascript and CSS issues in Safari.

* Tue Apr 06 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.2-3
- Add CSS for disabled button fallback classes.

* Tue Apr 06 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.2-2
- Add branding.

* Tue Apr 06 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.2-1
- Check for permission to configure Samba before setting up plugin.
- Check that smb.conf has `includes = registry` and report error if not.
- Fix crash when line in advanced configuration textarea does not include '='.

* Mon Apr 05 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.1-1
- Always clear timeout when setting a new info message.

* Thu Apr 01 2021 Josh Boudreau <jboudreau@45drives.com> 1.0.0-1
- First Build
