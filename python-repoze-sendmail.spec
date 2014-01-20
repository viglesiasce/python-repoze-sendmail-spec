%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-repoze-sendmail
Version:        4.1
Release:        0.1%{?dist}
Summary:        repoze.sendmail allows coupling the sending of email messages with a transaction, using the Zope transaction manager. 

License:        ZPL 2.1
URL:            https://pypi.python.org/pypi/repoze.sendmail
Source0:        https://pypi.python.org/packages/source/r/repoze.sendmail/repoze.sendmail-4.1.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-zope-interface
Requires:       python-transaction

%description
repoze.sendmail allows coupling the sending of email messages with a transaction, using the Zope transaction manager. This allows messages to only be sent out when and if a transaction is committed, preventing users from receiving notifications about events which may not have completed successfully.

%prep
%setup -q -n repoze.sendmail-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc README.rst
%doc docs/*
%{python_sitelib}/*
/usr/bin/qp

%changelog
* Mon Jan 20 2014 Vic Iglesias
- Initial release
