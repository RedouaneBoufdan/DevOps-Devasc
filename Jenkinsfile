pipeline {
  agent any

  environment {
    APP_DIR = "Flask/Pf3_microservice"
    IMAGE   = "j2-pf3-microservice"
    CNAME   = "j2-pf3-running"
    PORT    = "5051"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
        echo 'Source code checked out'
        sh 'pwd'
        sh 'ls -la'
      }
    }

    stage('Build') {
      steps {
        echo 'Build Docker image'
        sh '''
          cd "$APP_DIR"
          docker build -t "$IMAGE:1.0" .
        '''
      }
    }

    stage('Run') {
      steps {
        echo 'Run container'
        sh '''
          docker rm -f "$CNAME" 2>/dev/null || true
          docker run -d -p "$PORT:$PORT" --name "$CNAME" "$IMAGE:1.0"
          docker ps --filter "name=$CNAME"
        '''
      }
    }

    stage('Test') {
      steps {
        echo 'Test endpoints'
        sh '''
          # wait until service is ready
          for i in 1 2 3 4 5; do
            curl -s "http://localhost:$PORT/health" && echo "" && break
            sleep 2
          done

          curl -s -X POST "http://localhost:$PORT/strength" \
            -H "Content-Type: application/json" \
            -d '{"password":"Test123!"}' && echo ""

          curl -s -X POST "http://localhost:$PORT/hash" \
            -H "Content-Type: application/json" \
            -d '{"password":"Test123!"}' && echo ""
        '''
      }
    }
  }

  post {
    always {
      echo 'Cleanup'
      sh 'docker rm -f "$CNAME" 2>/dev/null || true'
    }
  }
}
