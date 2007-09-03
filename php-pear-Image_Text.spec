%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Text
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

%define	_beta beta
%define	_rel 1
Summary:	%{_pearname} - comfortable processing of texts in images
Summary(pl.UTF-8):	%{_pearname} - komfortowe przetwarzanie tekstu w obrazkach
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	0.%{_beta}.%{_rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_beta}.tgz
# Source0-md5:	11ef956fc2a93fd359a80bde7fc0e8e8
URL:		http://pear.php.net/package/Image_Text/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gd)
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

%description -l pl.UTF-8
Ta klasa pozwala na dodanie tekstu do dynamicznie generowanych
obrazków w sposób bardziej komfortowy niż dotychczas. Możliwe jest
przetwarzanie tekstów wielolinijkowych i manipulowanie:
- obramowaniem
- cieniem
- ustawieniem.
Inną ciekawą cechą jest pozwolenie klasie na zmierzenie tekstu w
zależności od rozmiaru czcionki i dzielenie go na linie, aby zmieścił
się w podanym polu tekstowym.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/example
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
