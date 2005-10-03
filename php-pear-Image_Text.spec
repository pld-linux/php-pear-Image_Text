%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Text
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - comfortable processing of texts in images
Summary(pl):	%{_pearname} - komfortowe przetwarzanie tekstu w obrazkach
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	2.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	84121838f5d3582225a64785ec63a4a5
URL:		http://pear.php.net/package/Image_Text/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-gd
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class allows you to add text to dynamic generated images more
comfortable. It allows you to process multiline text and manipulate:
- Border
- Shading
- Alignment
Another nice feature is to let the class measurize your text in respect
to font size and line splitting to fit a given text box.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa pozwala na dodanie tekstu do dynamicznie generowanych
obrazków w sposób bardziej komfortowy ni¿ dotychczas. Mo¿liwe jest
przetwarzanie tekstów wielolinijkowych i manipulowanie:
- obramowaniem
- cieniem
- ustawieniem.
Inn± ciekaw± cech± jest pozwolenie klasie na zmierzenie tekstu w
zale¿no¶ci od rozmiaru czcionki i dzielenie go na linie, aby zmie¶ci³
siê w podanym polu tekstowym.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
cp -a ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/example
%attr(755,root,root) %{_bindir}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
