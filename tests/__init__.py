#Run tests          : pytest src/tests -q
#coverage test      : pytest src/tests --cov="src"
#file test coverage : pytest src/tests/ --cov="src" --cov-report xml:coverage-reports/coverage.xml
#Nota               : En caso de generar un nuevo arhivo, modificar el source de la siguiente forma:
#	<sources>
#		<source>./src</source>
#	</sources>