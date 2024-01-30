import { Module } from "@nestjs/common";
import { SayajinController } from "./sayajin.controller";
import { SayajinService } from "./sayajin.service";

@Module({
    providers:[SayajinService],
    controllers:[SayajinController]
})

export class SayajinModule {}