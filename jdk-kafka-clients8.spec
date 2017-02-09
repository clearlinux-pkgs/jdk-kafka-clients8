Name     : jdk-kafka-clients8
Version  : 0.8.2.1
Release  : 2
URL      : http://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.jar
Source0  : http://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.jar
Source1  : http://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.pom
Source2  : kafka-clients-0.8.2.1.xml
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/kafka-clients-0.8.2.1.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/kafka-clients-0.8.2.1.pom
mv %{SOURCE2} %{buildroot}/usr/share/maven-metadata/kafka-clients-0.8.2.1.xml


%files
%defattr(-,root,root,-)
/usr/share/java/kafka-clients-0.8.2.1.jar
/usr/share/maven-metadata/kafka-clients-0.8.2.1.xml
/usr/share/maven-poms/kafka-clients-0.8.2.1.pom
