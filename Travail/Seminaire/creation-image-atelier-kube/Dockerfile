FROM gitlab-registry.insee.fr/kubernetes/images/run/java:21-rootless-jre

COPY --chown=$JAVA_USER:$JAVA_USER ./target/*.jar /usr/local/app.jar 

CMD [ "java", "-jar", "/usr/local/app.jar" ]