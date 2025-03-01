# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import interstellar_pb2 as interstellar__pb2


class InterstellarCommunicationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/interstellar.InterstellarCommunication/SayHello',
                request_serializer=interstellar__pb2.HelloRequest.SerializeToString,
                response_deserializer=interstellar__pb2.HelloResponse.FromString,
                )
        self.GetMessageFromMars = channel.unary_stream(
                '/interstellar.InterstellarCommunication/GetMessageFromMars',
                request_serializer=interstellar__pb2.MessageRequest.SerializeToString,
                response_deserializer=interstellar__pb2.StreamMessageFromMars.FromString,
                )
        self.SendMessageFromEarth = channel.stream_unary(
                '/interstellar.InterstellarCommunication/SendMessageFromEarth',
                request_serializer=interstellar__pb2.StreamMessageFromEarth.SerializeToString,
                response_deserializer=interstellar__pb2.ReplyFromMars.FromString,
                )
        self.SendAndReceiveMessage = channel.stream_stream(
                '/interstellar.InterstellarCommunication/SendAndReceiveMessage',
                request_serializer=interstellar__pb2.StreamMessageFromEarth.SerializeToString,
                response_deserializer=interstellar__pb2.StreamMessageFromMars.FromString,
                )


class InterstellarCommunicationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Say hello and receive a hello back
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMessageFromMars(self, request, context):
        """Get a stream of words from Mars
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageFromEarth(self, request_iterator, context):
        """Send a stream of words from earth and get a quick reply back from Mars
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendAndReceiveMessage(self, request_iterator, context):
        """Send a stream of words from earth and get a stream of words back from Mars
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InterstellarCommunicationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=interstellar__pb2.HelloRequest.FromString,
                    response_serializer=interstellar__pb2.HelloResponse.SerializeToString,
            ),
            'GetMessageFromMars': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMessageFromMars,
                    request_deserializer=interstellar__pb2.MessageRequest.FromString,
                    response_serializer=interstellar__pb2.StreamMessageFromMars.SerializeToString,
            ),
            'SendMessageFromEarth': grpc.stream_unary_rpc_method_handler(
                    servicer.SendMessageFromEarth,
                    request_deserializer=interstellar__pb2.StreamMessageFromEarth.FromString,
                    response_serializer=interstellar__pb2.ReplyFromMars.SerializeToString,
            ),
            'SendAndReceiveMessage': grpc.stream_stream_rpc_method_handler(
                    servicer.SendAndReceiveMessage,
                    request_deserializer=interstellar__pb2.StreamMessageFromEarth.FromString,
                    response_serializer=interstellar__pb2.StreamMessageFromMars.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'interstellar.InterstellarCommunication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InterstellarCommunication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/interstellar.InterstellarCommunication/SayHello',
            interstellar__pb2.HelloRequest.SerializeToString,
            interstellar__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMessageFromMars(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/interstellar.InterstellarCommunication/GetMessageFromMars',
            interstellar__pb2.MessageRequest.SerializeToString,
            interstellar__pb2.StreamMessageFromMars.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageFromEarth(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/interstellar.InterstellarCommunication/SendMessageFromEarth',
            interstellar__pb2.StreamMessageFromEarth.SerializeToString,
            interstellar__pb2.ReplyFromMars.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendAndReceiveMessage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/interstellar.InterstellarCommunication/SendAndReceiveMessage',
            interstellar__pb2.StreamMessageFromEarth.SerializeToString,
            interstellar__pb2.StreamMessageFromMars.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
