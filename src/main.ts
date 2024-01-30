import { NestFactory } from '@nestjs/core';
import { SayajinModule } from './sayajin/sayajin.module';

async function bootstrap() {
  const app = await NestFactory.create(SayajinModule);
  await app.listen(3000);
}
bootstrap();
