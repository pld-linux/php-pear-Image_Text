%include	/usr/lib/rpm/macros.php
%define         _class          Image
%define         _subclass       Text
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Comfortable processing of texts in images
Summary(pl):	%{_pearname} - Komfortowe przetwarzanie tekstu w obrazkach
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dc55343a37e1ac828ebc46f2b4b39c38
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class allows you to add text to dynamic generated images more comfortable.
It allows you to process multiline text and manipulate:
- Border
- Shading
- Aligniment
Another nice feature is to let the class measurize your text in respect to font size and
line splitting to fit a given text box.

This class has in PEAR status: %{_status}.

#%description -l pl
#
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{doc,example}
%{php_pear_dir}/%{_class}/*.php
