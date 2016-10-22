%{?scl:%scl_package javaewah}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

%global commit c6a7fca48eb10572c57e8f644c11633456611d8f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           %{?scl_prefix}javaewah
Version:        0.8.4
Release:        6.%{baserelease}%{?dist}
Summary:        A word-aligned compressed variant of the Java bitset class

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://code.google.com/p/javaewah/
Source0:        https://github.com/lemire/%{pkg_name}/archive/%{commit}/%{pkg_name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires: %{?scl_prefix_maven}maven-local
BuildRequires: %{?scl_prefix_maven}maven-surefire-provider-junit

%description
JavaEWAH is a word-aligned compressed variant of the Java bitset class.
It uses a 64-bit run-length encoding (RLE) compression scheme.

The goal of word-aligned compression is not to achieve the best
compression, but rather to improve query processing time. Hence, we try
to save CPU cycles, maybe at the expense of storage. However, the EWAH
scheme we implemented is always more efficient storage-wise than an
uncompressed bitmap (implemented in Java as the BitSet class). Unlike
some alternatives, javaewah does not rely on a patented scheme.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -n %{pkg_name}-%{version} -qn %{pkg_name}-%{commit}

%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc CHANGELOG README.md LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Thu Jul 21 2016 Mat Booth <mat.booth@redhat.com> - 0.8.4-6.1
- Auto SCL-ise package for rh-eclipse46 collection

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mat Booth <mat.booth@redhat.com> - 0.8.4-5
- Fix FTBFS due to strict javadoc linting

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Alexander Kurtakov <akurtako@redhat.com> 0.8.4-2
- Surefire junit provider is a single package now.

* Sat Mar 22 2014 Gerard Ryan <galileo@fedoraproject.org> - 0.8.4-1
- Update to upstream version 0.8.4
- Re-enable tests

* Sat Nov 16 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.7.9-2
- Skip tests since they prevent building in koji

* Sat Nov 16 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.7.9-1
- Update to 0.7.9 to fix license ambiguity

* Thu Oct 10 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.7.8-1
- Update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.6.12-1
- Initial package.